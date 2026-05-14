"use client";

import { createPortal } from "react-dom";
import { useLayoutEffect, useState } from "react";
import type { TocTreeNode } from "@/lib/markdown-toc";
import PostToc from "@/components/PostToc";

const SLOT_ID = "post-toc-slot";

/** 将本页目录 + 歌词挂到根布局右侧栏，与标签树同列 */
export default function PostTocPortal({ tree }: { tree: TocTreeNode[] }) {
  const [slot, setSlot] = useState<HTMLElement | null>(null);

  useLayoutEffect(() => {
    setSlot(document.getElementById(SLOT_ID));
  }, []);

  if (!tree.length) return null;
  if (!slot) return null;
  return createPortal(<PostToc tree={tree} />, slot);
}
