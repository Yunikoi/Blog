"use client";

import { useEffect } from "react";
import { usePathname } from "next/navigation";

/** 修复 SPA 内 hash 锚点不滚动；与目录链接配合 */
export default function HashScroll() {
  const pathname = usePathname();
  useEffect(() => {
    const run = () => {
      const raw = window.location.hash?.slice(1);
      if (!raw) return;
      let id = raw;
      try {
        id = decodeURIComponent(raw);
      } catch {
        /* keep raw */
      }
      let el = document.getElementById(id);
      if (!el && typeof CSS !== "undefined" && typeof CSS.escape === "function") {
        el = document.querySelector(`[id="${CSS.escape(id)}"]`);
      }
      requestAnimationFrame(() => el?.scrollIntoView({ behavior: "smooth", block: "start" }));
    };
    run();
    window.addEventListener("hashchange", run);
    return () => window.removeEventListener("hashchange", run);
  }, [pathname]);
  return null;
}
