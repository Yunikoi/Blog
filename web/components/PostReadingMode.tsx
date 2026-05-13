"use client";

import { useEffect, useState } from "react";

export default function PostReadingMode({ children }: { children: React.ReactNode }) {
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    document.documentElement.classList.add("reading-mode");
    return () => {
      document.documentElement.classList.remove("reading-mode", "reading-mode--expanded");
    };
  }, []);

  useEffect(() => {
    if (expanded) document.documentElement.classList.add("reading-mode--expanded");
    else document.documentElement.classList.remove("reading-mode--expanded");
  }, [expanded]);

  return (
    <>
      {children}
      <button
        type="button"
        className="reading-mode-toggle"
        onClick={() => setExpanded((v) => !v)}
        aria-pressed={expanded}
        title={expanded ? "恢复沉浸阅读" : "展开侧栏与目录"}
      >
        {expanded ? "沉浸" : "侧栏"}
      </button>
    </>
  );
}
