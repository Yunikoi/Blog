import Link from "next/link";
import { getSiteInfo, listPosts } from "@/lib/posts";

export const dynamic = "force-dynamic";

export default async function HomePage() {
  const { blogName, blogDescription } = await getSiteInfo();
  const posts = await listPosts();

  return (
    <div className="wrap">
      <nav className="nav">
        <Link href="/">首页</Link>
      </nav>
      <header>
        <h1 style={{ margin: "0 0 0.5rem" }}>{blogName}</h1>
        {blogDescription ? <p style={{ color: "var(--muted)", margin: 0 }}>{blogDescription}</p> : null}
      </header>
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
