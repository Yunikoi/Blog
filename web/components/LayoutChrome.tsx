"use client";

import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";

type Anim = "none" | "enter-up" | "exit-down";

/** 顶栏 + 主体整体：进入文章向上、离开文章向下 */
export default function LayoutChrome({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [anim, setAnim] = useState<Anim>("none");
  const prevRef = useRef<string | null>(null);
  const hydratedRef = useRef(false);

  useEffect(() => {
    if (!hydratedRef.current) {
      hydratedRef.current = true;
      prevRef.current = pathname;
      if (pathname.startsWith("/posts/")) setAnim("enter-up");
      return;
    }

    const prev = prevRef.current ?? "";
    prevRef.current = pathname;

    const wasPost = prev.startsWith("/posts/");
    const isPost = pathname.startsWith("/posts/");
    if (!wasPost && isPost) setAnim("enter-up");
    else if (wasPost && !isPost) setAnim("exit-down");
    else setAnim("none");
  }, [pathname]);

  useEffect(() => {
    if (anim === "none") return;
    const id = window.setTimeout(() => setAnim("none"), 680);
    return () => window.clearTimeout(id);
  }, [anim]);

  const cls = ["layout-chrome", anim === "enter-up" ? "layout-chrome--enter-up" : "", anim === "exit-down" ? "layout-chrome--exit-down" : ""]
    .filter(Boolean)
    .join(" ");

  return <div className={cls}>{children}</div>;
}
