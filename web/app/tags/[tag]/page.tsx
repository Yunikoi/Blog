import Link from "next/link";
import { listPostsByTag } from "@/lib/posts";

export const dynamic = "force-dynamic";

type Props = { params: { tag: string } };

export default async function TagDetailPage({ params }: Props) {
  const tag = decodeURIComponent(params.tag);
  const posts = await listPostsByTag(tag);

  return (
    <div className="wrap">
      <p className="meta">
        <Link href="/tags">← 全部标签</Link>
      </p>
      <h1>「{tag}」</h1>
      {posts.length === 0 ? (
        <p style={{ color: "var(--muted)" }}>该标签下暂无文章。</p>
      ) : (
        <ul className="post-list">
          {posts.map((p) => (
            <li key={p.slug}>
              <Link href={`/posts/${encodeURIComponent(p.slug)}`}>{p.title}</Link>
              <div className="meta">
                {p.date || ""}
                {p.updated && p.updated !== p.date ? ` · 更新 ${p.updated}` : ""}
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
