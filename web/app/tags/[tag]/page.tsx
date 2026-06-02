import Link from "next/link";
import { listPostsByTag } from "@/lib/posts";

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
      <p className="meta">含子标签下的文章。</p>
      {posts.length === 0 ? (
        <p style={{ color: "var(--muted)" }}>该标签下暂无文章。</p>
      ) : (
        <ul className="post-list">
          {posts.map((p) => (
            <li key={p.slug} className="post-card-wrap">
              <div className="post-card-main">
                <Link href={`/posts/${encodeURIComponent(p.slug)}`}>{p.title}</Link>
                <div className="meta">
                  {p.column ? <span className="post-col-badge">{p.column}</span> : null}
                  {p.column && (p.date || p.updated) ? <span> · </span> : null}
                  {p.date || ""}
                  {p.updated && p.updated !== p.date ? ` · 更新 ${p.updated}` : ""}
                  {p.tags?.length ? (
                    <span>
                      {p.date || p.updated ? " · " : null}
                      {p.tags.join(" · ")}
                    </span>
                  ) : null}
                </div>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
