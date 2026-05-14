import type { TocTreeNode } from "@/lib/markdown-toc";

import PostTocLyrics from "@/components/PostTocLyrics";

function TocBranch({ nodes, depth }: { nodes: TocTreeNode[]; depth?: number }) {
  if (!nodes.length) return null;
  const d = depth ?? 0;
  return (
    <ul className={d === 0 ? "post-toc__list post-toc__list--root" : "post-toc__nest"}>
      {nodes.map((n) => (
        <li key={n.id} className="post-toc__node">
          <a href={`#${encodeURIComponent(n.id)}`}>{n.text}</a>
          {n.children.length > 0 ? <TocBranch nodes={n.children} depth={d + 1} /> : null}
        </li>
      ))}
    </ul>
  );
}

export default function PostToc({ tree }: { tree: TocTreeNode[] }) {
  if (!tree.length) return null;
  return (
    <nav className="post-toc" aria-label="本页目录">
      <p className="post-toc__title">目录</p>
      <div className="post-toc__tree-wrap">
        <TocBranch nodes={tree} />
      </div>
      <PostTocLyrics />
    </nav>
  );
}
