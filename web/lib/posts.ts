import fs from "fs/promises";
import path from "path";
import matter from "gray-matter";
import { getContentDir } from "@/lib/content-dir";

/** gray-matter 会把 YAML 日期解析成 Date，排序/字符串化前统一成 YYYY-MM-DD 或原字符串 */
function normalizeFrontmatterDate(value: unknown): string | undefined {
  if (value == null || value === "") return undefined;
  if (value instanceof Date) {
    if (Number.isNaN(value.getTime())) return undefined;
    return value.toISOString().slice(0, 10);
  }
  if (typeof value === "string") return value.trim() || undefined;
  if (typeof value === "number") return String(value);
  return String(value);
}

function paths() {
  const CONTENT_DIR = getContentDir();
  return {
    CONTENT_DIR,
    POSTS_DIR: path.join(CONTENT_DIR, "posts"),
    TAGS_FILE: path.join(CONTENT_DIR, "tags.json"),
    MANIFEST_FILE: path.join(CONTENT_DIR, "manifest.json"),
  };
}

export type PostMeta = {
  slug: string;
  title: string;
  date?: string;
  tags: string[];
  excerpt?: string;
};

async function readTagsMap(): Promise<Record<string, string[]>> {
  const { TAGS_FILE } = paths();
  try {
    const raw = await fs.readFile(TAGS_FILE, "utf8");
    const j = JSON.parse(raw) as Record<string, unknown>;
    const out: Record<string, string[]> = {};
    for (const [k, v] of Object.entries(j)) {
      if (Array.isArray(v)) out[k] = v.map(String);
      else if (typeof v === "string") out[k] = v.split(/,\s*/).filter(Boolean);
    }
    return out;
  } catch {
    return {};
  }
}

async function readManifest(): Promise<{ blogName?: string; blogDescription?: string }> {
  const { MANIFEST_FILE } = paths();
  try {
    const raw = await fs.readFile(MANIFEST_FILE, "utf8");
    return JSON.parse(raw) as { blogName?: string; blogDescription?: string };
  } catch {
    return {};
  }
}

export async function getSiteInfo() {
  const m = await readManifest();
  return {
    blogName: m.blogName || "纸间",
    blogDescription: m.blogDescription || "",
  };
}

export async function listPosts(): Promise<PostMeta[]> {
  const { POSTS_DIR } = paths();
  const tagsMap = await readTagsMap();
  let names: string[] = [];
  try {
    names = (await fs.readdir(POSTS_DIR)).filter((f) => f.endsWith(".md"));
  } catch {
    return [];
  }
  const posts: PostMeta[] = [];
  for (const file of names) {
    try {
      const slug = file.replace(/\.md$/i, "");
      const full = path.join(POSTS_DIR, file);
      const raw = await fs.readFile(full, "utf8");
      const { data, content } = matter(raw);
      const title = (data.title as string) || slug;
      const date = normalizeFrontmatterDate(data.date);
      const excerpt =
        (data.excerpt as string) ||
        content.replace(/^---[\s\S]*?---\s*/m, "").slice(0, 160).replace(/\s+/g, " ").trim();
      posts.push({
        slug,
        title,
        date,
        tags: tagsMap[slug] || [],
        excerpt,
      });
    } catch (e) {
      console.error("[listPosts] skip file", file, e);
    }
  }
  posts.sort((a, b) => String(b.date || "").localeCompare(String(a.date || "")));
  return posts;
}

export async function getPost(slug: string) {
  const { POSTS_DIR } = paths();
  const safe = slug.replace(/[^a-zA-Z0-9._-]/g, "");
  if (safe !== slug) return null;
  const full = path.join(POSTS_DIR, `${safe}.md`);
  try {
    const raw = await fs.readFile(full, "utf8");
    let data: Record<string, unknown> = {};
    let content = raw;
    try {
      const parsed = matter(raw);
      data = parsed.data as Record<string, unknown>;
      content = parsed.content;
    } catch (e) {
      console.error("[getPost] matter failed", slug, e);
      return null;
    }
    const tagsMap = await readTagsMap();
    return {
      slug: safe,
      title: (data.title as string) || safe,
      date: normalizeFrontmatterDate(data.date),
      tags: tagsMap[safe] || [],
      content,
    };
  } catch {
    return null;
  }
}

export async function listPostsByTag(tag: string): Promise<PostMeta[]> {
  const t = String(tag || "").trim();
  if (!t) return [];
  const all = await listPosts();
  return all.filter((p) => (p.tags || []).includes(t));
}

export async function allTags(): Promise<string[]> {
  const posts = await listPosts();
  const set = new Set<string>();
  posts.forEach((p) => (p.tags || []).forEach((t) => set.add(t)));
  return [...set].sort((a, b) => a.localeCompare(b, "zh-CN"));
}

export function publicSiteOrigin(): string {
  if (process.env.BLOG_PUBLIC_URL) return process.env.BLOG_PUBLIC_URL.replace(/\/$/, "");
  if (process.env.VERCEL_URL) return `https://${process.env.VERCEL_URL.replace(/\/$/, "")}`;
  return "http://localhost:3000";
}
