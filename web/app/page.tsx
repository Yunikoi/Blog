import Link from "next/link";
import { getSiteInfo, listPosts } from "@/lib/posts";

export default async function HomePage() {
  const { blogDescription } = await getSiteInfo();
  const posts = await listPosts();

  return (
    <div className="wrap">
      <header className="page-intro">
        {blogDescription ? <p className="lead">{blogDescription}</p> : null}
      </header>
      <h1 className="page-title">文章</h1>
      <ul className="post-list">
        {posts.map((p) => (
          <li key={p.slug} className="post-card-wrap">
            <div className="post-card-main">
              <Link href={`/posts/${encodeURIComponent(p.slug)}`}>{p.title}</Link>
              <div className="meta">
                {p.column ? <span className="post-col-badge">{p.column}</span> : null}
                {p.column && (p.date || p.updated || p.tags?.length) ? <span> · </span> : null}
                {p.date ? <span>{p.date}</span> : null}
                {p.updated && p.updated !== p.date ? (
                  <span>
                    {p.date ? " · " : null}
                    更新 {p.updated}
                  </span>
                ) : null}
                {p.tags?.length ? (
                  <span>
                    {p.date || p.updated ? " · " : null}
                    {p.tags.join(" · ")}
                  </span>
                ) : null}
              </div>
              {p.excerpt ? <p className="post-excerpt-inline">{p.excerpt}</p> : null}
            </div>
          </li>
        ))}
      </ul>
      {posts.length === 0 ? <p style={{ color: "var(--muted)" }}>暂无文章（请确认 content/posts 下有 .md 文件）。</p> : null}
    </div>
  );
}
