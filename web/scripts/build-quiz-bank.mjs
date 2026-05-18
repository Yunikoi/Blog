/**
 * 从 content/posts 生成 public/quiz-bank.json，部署后任意网络可访问 /quiz（无需本机 API）。
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import matter from "gray-matter";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const webRoot = path.join(__dirname, "..");
const postsDir = path.join(webRoot, "content", "posts");
const outFile = path.join(webRoot, "public", "quiz-bank.json");

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w\u4e00-\u9fff-]+/g, "")
    .slice(0, 80);
}

function splitTermDefinition(body) {
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

function extractCards(markdown, deckSlug, deckTitle) {
  const cards = [];
  const seen = new Set();
  for (const line of markdown.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed.startsWith("#### ")) continue;
    const body = trimmed.slice(5).trim();
    const split = splitTermDefinition(body);
    if (!split) continue;
    const { term, definition } = split;
    if (term.length < 1 || term.length > 120 || definition.length < 1) continue;
    const id = `${deckSlug}::${slugify(term)}`;
    if (seen.has(id)) continue;
    seen.add(id);
    cards.push({ id, deckSlug, deckTitle, term, definition });
  }
  return cards;
}

if (!fs.existsSync(postsDir)) {
  console.warn("[build-quiz-bank] 无 content/posts，跳过");
  process.exit(0);
}

const decks = [];
for (const file of fs.readdirSync(postsDir)) {
  if (!/\.md$/i.test(file)) continue;
  const slug = file.replace(/\.md$/i, "");
  try {
    const raw = fs.readFileSync(path.join(postsDir, file), "utf8");
    const { data, content } = matter(raw);
    const title = data.title || slug;
    const cards = extractCards(content, slug, title);
    if (cards.length > 0) decks.push({ slug, title, cards });
  } catch (e) {
    console.warn("[build-quiz-bank] skip", file, e.message);
  }
}

decks.sort((a, b) => String(a.title).localeCompare(String(b.title), "zh-CN"));

const bank = {
  version: 1,
  generatedAt: new Date().toISOString(),
  decks,
};

fs.mkdirSync(path.dirname(outFile), { recursive: true });
fs.writeFileSync(outFile, JSON.stringify(bank), "utf8");
const total = decks.reduce((n, d) => n + d.cards.length, 0);
console.log(`[build-quiz-bank] ${decks.length} 个词库，共 ${total} 词 → public/quiz-bank.json`);
