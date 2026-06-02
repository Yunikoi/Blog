import Link from "next/link";
import { allTags } from "@/lib/posts";

export default async function TagsPage() {
  const tags = await allTags();
  return (
    <div className="wrap">
      <h1>标签</h1>
      <p className="meta">标签来自文章 frontmatter，多级标签可用 <code>/</code> 分隔；点击树或下方链接筛选文章。</p>
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
