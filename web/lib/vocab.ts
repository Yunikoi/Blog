import fs from "fs/promises";
import path from "path";
import matter from "gray-matter";
import { getContentDir } from "@/lib/content-dir";
import { listPosts } from "@/lib/posts";
import type { VocabCard } from "@/lib/vocab-core";

export type { VocabCard } from "@/lib/vocab-core";
export { buildChoices, shuffle } from "@/lib/vocab-core";

export type VocabDeckMeta = {
  slug: string;
  title: string;
  count: number;
};

/** 从 `#### 词：释义` 行提取词条（与 0427-Learning / Yasi 等笔记格式一致） */
export function extractVocabCardsFromMarkdown(
  markdown: string,
  deckSlug: string,
  deckTitle: string
): VocabCard[] {
  const cards: VocabCard[] = [];
  const seen = new Set<string>();

  for (const line of markdown.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed.startsWith("#### ")) continue;

    const body = trimmed.slice(5).trim();
    const split = splitTermDefinition(body);
    if (!split) continue;

    const { term, definition } = split;
    if (term.length < 1 || term.length > 120) continue;
    if (definition.length < 1) continue;

    const id = `${deckSlug}::${slugify(term)}`;
    if (seen.has(id)) continue;
    seen.add(id);

    cards.push({ id, deckSlug, deckTitle, term, definition });
  }

  return cards;
}

function splitTermDefinition(body: string): { term: string; definition: string } | null {
  const idxCn = body.indexOf("：");
  const idxEn = body.indexOf(":");
  let idx = -1;
  if (idxCn >= 0 && idxEn >= 0) idx = Math.min(idxCn, idxEn);
  else if (idxCn >= 0) idx = idxCn;
  else if (idxEn >= 0) idx = idxEn;
  if (idx <= 0) return null;

  const term = body.slice(0, idx).trim();
  const definition = body.slice(idx + 1).trim();
  if (!term || !definition) return null;
  return { term, definition };
}

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w\u4e00-\u9fff-]+/g, "")
    .slice(0, 80);
}

export async function loadDeckCards(deckSlug: string): Promise<VocabCard[]> {
  const { POSTS_DIR } = vocabPaths();
  const full = path.join(POSTS_DIR, `${deckSlug}.md`);
  const raw = await fs.readFile(full, "utf8");
  const { data, content } = matter(raw);
  const title = (data.title as string) || deckSlug;
  return extractVocabCardsFromMarkdown(content, deckSlug, title);
}

export async function listVocabDecks(): Promise<VocabDeckMeta[]> {
  const posts = await listPosts();
  const decks: VocabDeckMeta[] = [];

  for (const p of posts) {
    try {
      const cards = await loadDeckCards(p.slug);
      if (cards.length > 0) {
        decks.push({ slug: p.slug, title: p.title, count: cards.length });
      }
    } catch {
      /* skip unreadable */
    }
  }

  decks.sort((a, b) => a.title.localeCompare(b.title, "zh-CN"));
  return decks;
}

export async function loadAllCards(deckSlug?: string): Promise<VocabCard[]> {
  if (deckSlug) return loadDeckCards(deckSlug);
  const decks = await listVocabDecks();
  const all: VocabCard[] = [];
  for (const d of decks) {
    all.push(...(await loadDeckCards(d.slug)));
  }
  return all;
}

function vocabPaths() {
  const CONTENT_DIR = getContentDir();
  return { CONTENT_DIR, POSTS_DIR: path.join(CONTENT_DIR, "posts") };
}
