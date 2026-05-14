"use client";

import { usePathname } from "next/navigation";

/** 仅包裹 `<main>` 内路由片段，切换时用模糊渐入避免牵动顶栏与侧栏 */
export default function MainShellTransition({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  return (
    <main className="main-shell">
      <div key={pathname} className="main-shell__page">
        {children}
      </div>
    </main>
  );
}
