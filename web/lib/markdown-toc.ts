import GithubSlugger from "github-slugger";
import { headingRank } from "hast-util-heading-rank";
import { toString } from "hast-util-to-string";
import type { Element, Root as HastRoot } from "hast";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import { unified } from "unified";
import { visit } from "unist-util-visit";

export type TocItem = { depth: number; text: string; id: string };

/**
 * 用与正文相同的 remark → rehype 管线取标题文本（hast toString），
 * 再用 GitHubSlugger 生成 id，与 ReactMarkdown + rehype-slug 一致，避免 mdast 与 hast 文本不一致导致目录无法跳转。
 */
export function extractToc(markdown: string): TocItem[] {
  const processor = unified().use(remarkParse).use(remarkGfm).use(remarkRehype);
  const tree = processor.runSync(processor.parse(markdown)) as HastRoot;
  const slugger = new GithubSlugger();
  const toc: TocItem[] = [];
  visit(tree, "element", (node: Element) => {
    const rank = headingRank(node);
    if (!rank) return;
    const text = toString(node).trim();
    if (!text) return;
    const id = slugger.slug(text);
    toc.push({ depth: rank, text, id });
  });
  return toc;
}
