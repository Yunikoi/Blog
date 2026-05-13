import GithubSlugger from "github-slugger";
import { toString } from "mdast-util-to-string";
import type { Heading, Root } from "mdast";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import { unified } from "unified";
import { visit } from "unist-util-visit";

export type TocItem = { depth: number; text: string; id: string };

/** 与 rehype-slug 一致：同一篇内用 GitHubSlugger 生成锚点（正文标题可点击跳转） */
export function extractToc(markdown: string): TocItem[] {
  const tree = unified().use(remarkParse).use(remarkGfm).parse(markdown) as Root;
  const slugger = new GithubSlugger();
  const toc: TocItem[] = [];
  visit(tree, "heading", (node: Heading) => {
    const text = toString(node).trim();
    if (!text) return;
    const id = slugger.slug(text);
    toc.push({ depth: node.depth, text, id });
  });
  return toc;
}
