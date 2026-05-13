import Link from "next/link";
import type { TagTrieNode } from "@/lib/tag-tree";

function RenderNodes({ nodes }: { nodes: TagTrieNode[] }) {
  return (
    <ul className="tag-tree-list">
      {nodes.map((n) => (
        <li key={`${n.segment}-${n.fullTag || "b"}`}>
          {n.children.length > 0 ? (
            <details className="tag-tree-details">
              <summary className="tag-tree-summary">{n.segment}</summary>
              <RenderNodes nodes={n.children} />
            </details>
          ) : n.fullTag ? (
            <Link href={`/tags/${encodeURIComponent(n.fullTag)}`} className="tag-tree-link">
              {n.segment}
            </Link>
          ) : (
            <span className="tag-tree-leaf">{n.segment}</span>
          )}
        </li>
      ))}
    </ul>
  );
}

export default function TagTree({ nodes }: { nodes: TagTrieNode[] }) {
  if (!nodes.length) {
    return (
      <nav className="tag-tree" aria-label="标签">
        <p className="tag-tree__empty">暂无标签（可在 <code>tags.json</code> 配置；多级可用 <code>/</code> 或 <code>／</code> 分隔）。</p>
      </nav>
    );
  }

  return (
    <nav className="tag-tree" aria-label="标签树">
      <p className="tag-tree__title">标签</p>
      <RenderNodes nodes={nodes} />
    </nav>
  );
}
