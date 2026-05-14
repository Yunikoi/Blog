"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { TocTreeNode } from "@/lib/markdown-toc";

import PostTocLyrics from "@/components/PostTocLyrics";

/** 与顶栏高度大致对齐：标题滚过该线即视为「当前节」 */
const SCROLL_MARK_TOP_PX = 96;

function tocIdSetFromTree(nodes: TocTreeNode[]): Set<string> {
  const s = new Set<string>();
  const walk = (ns: TocTreeNode[]) => {
    for (const n of ns) {
      s.add(n.id);
      walk(n.children);
    }
  };
  walk(nodes);
  return s;
}

function pickActiveHeadingId(article: Element, tocIds: Set<string>): string | null {
  const headings = [...article.querySelectorAll("h1, h2, h3, h4, h5, h6")].filter(
    (el): el is HTMLElement => el.id !== "" && tocIds.has(el.id)
  );
  if (!headings.length) return null;
  let active: string | null = null;
  for (const h of headings) {
    if (h.getBoundingClientRect().top <= SCROLL_MARK_TOP_PX) active = h.id;
  }
  return active ?? headings[0].id;
}

function TocBranch({
  nodes,
  depth,
  activeId,
}: {
  nodes: TocTreeNode[];
  depth?: number;
  activeId: string | null;
}) {
  if (!nodes.length) return null;
  const d = depth ?? 0;
  return (
    <ul className={d === 0 ? "post-toc__list post-toc__list--root" : "post-toc__nest"}>
      {nodes.map((n) => (
        <li key={n.id} className="post-toc__node">
          <a
            href={`#${encodeURIComponent(n.id)}`}
            data-toc={n.id}
            className={activeId === n.id ? "post-toc__link--active" : undefined}
            aria-current={activeId === n.id ? "location" : undefined}
          >
            {n.text}
          </a>
          {n.children.length > 0 ? <TocBranch nodes={n.children} depth={d + 1} activeId={activeId} /> : null}
        </li>
      ))}
    </ul>
  );
}

export default function PostToc({ tree }: { tree: TocTreeNode[] }) {
  const tocIds = useMemo(() => tocIdSetFromTree(tree), [tree]);
  const [activeId, setActiveId] = useState<string | null>(null);
  const treeWrapRef = useRef<HTMLDivElement>(null);

  const syncFromScroll = useCallback(() => {
    const article = document.querySelector(".post-article-main");
    if (!article) return;
    const id = pickActiveHeadingId(article, tocIds);
    if (id) setActiveId((prev) => (prev === id ? prev : id));
  }, [tocIds]);

  useEffect(() => {
    syncFromScroll();
    let raf = 0;
    const onScroll = () => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(syncFromScroll);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      cancelAnimationFrame(raf);
    };
  }, [syncFromScroll]);

  useEffect(() => {
    const fromHash = () => {
      const raw = window.location.hash?.slice(1);
      if (!raw) return;
      let id = raw;
      try {
        id = decodeURIComponent(raw);
      } catch {
        /* keep raw */
      }
      if (tocIds.has(id)) setActiveId(id);
    };
    fromHash();
    window.addEventListener("hashchange", fromHash);
    return () => window.removeEventListener("hashchange", fromHash);
  }, [tocIds]);

  useEffect(() => {
    if (!activeId || !treeWrapRef.current) return;
    const wrap = treeWrapRef.current;
    const esc =
      typeof CSS !== "undefined" && typeof CSS.escape === "function"
        ? CSS.escape(activeId)
        : activeId.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
    const a = wrap.querySelector<HTMLAnchorElement>(`a[data-toc="${esc}"]`);
    a?.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }, [activeId]);

  if (!tree.length) return null;
  return (
    <nav className="post-toc" aria-label="本页目录">
      <p className="post-toc__title">目录</p>
      <div ref={treeWrapRef} className="post-toc__tree-wrap">
        <TocBranch nodes={tree} activeId={activeId} />
      </div>
      <PostTocLyrics />
    </nav>
  );
}
