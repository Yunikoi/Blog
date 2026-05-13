import Link from "next/link";
import { getSiteInfo, listPosts } from "@/lib/posts";

export const dynamic = "force-dynamic";

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
          <li key={p.slug}>
            <Link href={`/posts/${encodeURIComponent(p.slug)}`}>{p.title}</Link>
            <div className="meta">
              {p.date ? <span>{p.date}</span> : null}
              {p.tags?.length ? (
                <span>
                  {p.date ? " · " : null}
                  {p.tags.join(" · ")}
                </span>
              ) : null}
            </div>
            {p.excerpt ? <p style={{ color: "var(--muted)", fontSize: "0.95rem", margin: "0.5rem 0 0" }}>{p.excerpt}</p> : null}
          </li>
        ))}
      </ul>
      {posts.length === 0 ? <p style={{ color: "var(--muted)" }}>暂无文章（请确认 content/posts 下有 .md 文件）。</p> : null}
    </div>
  );
}
