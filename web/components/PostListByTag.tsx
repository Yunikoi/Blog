import Link from "next/link";
import type { PostGroup } from "@/lib/post-groups";

function PostRow({ p }: { p: PostGroup["posts"][number] }) {
  return (
    <li className="post-card-wrap">
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
  );
}

function GroupSection({ group, depth }: { group: PostGroup; depth: number }) {
  const Heading = depth === 0 ? "h2" : depth === 1 ? "h3" : "h4";
  const cls =
    depth === 0 ? "post-group post-group--root" : depth === 1 ? "post-group post-group--sub" : "post-group post-group--leaf";

  return (
    <section className={cls}>
      <Heading className="post-group__title">
        <Link href={`/tags/${encodeURIComponent(group.fullTag)}`} className="post-group__link">
          {group.name}
        </Link>
      </Heading>
      {group.posts.length > 0 ? (
        <ul className="post-list">
          {group.posts.map((p) => (
            <PostRow key={p.slug} p={p} />
          ))}
        </ul>
      ) : null}
      {group.children.length > 0 ? (
        <div className="post-group__children">
          {group.children.map((child) => (
            <GroupSection key={child.fullTag} group={child} depth={depth + 1} />
          ))}
        </div>
      ) : null}
    </section>
  );
}

export default function PostListByTag({ groups }: { groups: PostGroup[] }) {
  if (!groups.length) {
    return <p style={{ color: "var(--muted)" }}>暂无文章（请确认 content/posts 下有 .md 文件）。</p>;
  }
  return (
    <div className="post-groups">
      {groups.map((g) => (
        <GroupSection key={g.fullTag} group={g} depth={0} />
      ))}
    </div>
  );
}
