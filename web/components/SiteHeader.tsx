import Link from "next/link";
import { getSiteInfo } from "@/lib/posts";

export default async function SiteHeader() {
  const { blogName } = await getSiteInfo();
  return (
    <header className="site-header">
      <div className="site-header__inner">
        <Link href="/" className="site-logo">
          {blogName}
        </Link>
        <nav className="site-nav" aria-label="主导航">
          <Link href="/">首页</Link>
          <Link href="/tags">标签</Link>
          <Link href="/about">关于</Link>
          <Link href="/feed.xml">RSS</Link>
        </nav>
      </div>
    </header>
  );
}
