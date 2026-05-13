import type { TocItem } from "@/lib/markdown-toc";

export default function PostToc({ items }: { items: TocItem[] }) {
  if (!items.length) return null;
  return (
    <nav className="post-toc" aria-label="本页目录">
      <p className="post-toc__title">目录</p>
      <ul className="post-toc__list">
        {items.map((item, i) => (
          <li key={`toc-${i}-${item.id}`} className={`post-toc__item post-toc__item--d${item.depth}`}>
            <a href={`#${item.id}`}>{item.text}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
