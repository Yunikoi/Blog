"use client";

import { usePathname } from "next/navigation";
import { useEffect, useRef } from "react";

/**
 * 路由切换时在主内容区做一次轻量淡入（不 remount 子树，避免打断 Link / RSC）。
 * 首次进入站点不播放，避免首屏闪烁。
 */
export default function MainShellTransition({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const shellRef = useRef<HTMLDivElement>(null);
  const firstRef = useRef(true);
  const prevPathRef = useRef(pathname);

  useEffect(() => {
    const el = shellRef.current;
    if (!el) return;

    if (firstRef.current) {
      firstRef.current = false;
      prevPathRef.current = pathname;
      return;
    }

    if (prevPathRef.current === pathname) return;
    prevPathRef.current = pathname;

    el.classList.remove("main-shell__page--enter");
    void el.offsetWidth;
    el.classList.add("main-shell__page--enter");
    const id = window.setTimeout(() => {
      el.classList.remove("main-shell__page--enter");
    }, 240);
    return () => window.clearTimeout(id);
  }, [pathname]);

  return (
    <main className="main-shell">
      <div ref={shellRef} className="main-shell__page">
        {children}
      </div>
    </main>
  );
}
