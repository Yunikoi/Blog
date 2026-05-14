import Link from "next/link";
import { allTags } from "@/lib/posts";

export default async function TagsPage() {
  const tags = await allTags();
  return (
    <div className="wrap">
      <h1>标签</h1>
      <p className="meta">标签来自 <code>content/tags.json</code>，每次请求在服务端重新聚合。</p>
      <ul className="tag-cloud">
        {tags.map((t) => (
          <li key={t}>
            <Link href={`/tags/${encodeURIComponent(t)}`} className="tag-link">
              {t}
            </Link>
          </li>
        ))}
      </ul>
      {tags.length === 0 ? <p style={{ color: "var(--muted)" }}>暂无标签。</p> : null}
    </div>
  );
}
