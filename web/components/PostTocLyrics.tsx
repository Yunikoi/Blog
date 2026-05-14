"use client";

import { useEffect, useRef } from "react";
import { useMusicLyricsView } from "@/lib/music-lyrics-store";

export default function PostTocLyrics() {
  const view = useMusicLyricsView();
  const lineRefs = useRef<(HTMLParagraphElement | null)[]>([]);

  const { hasTracks, lrcLines, plainLyrics, activeLineIndex, lrcErr, lyricsReady, metaHint } = view;

  useEffect(() => {
    lineRefs.current = [];
  }, [lrcLines, plainLyrics]);

  useEffect(() => {
    if (activeLineIndex < 0) return;
    const el = lineRefs.current[activeLineIndex];
    el?.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }, [activeLineIndex]);

  if (!hasTracks) {
    return (
      <div className="post-toc__lyrics" aria-label="歌词">
        <p className="post-toc__lyrics-placeholder">播放音乐时，歌词显示在此区域</p>
      </div>
    );
  }

  return (
    <div className="post-toc__lyrics" role="log" aria-live="polite" aria-label="歌词">
      {metaHint ? <p className="post-toc__lyrics-meta">{metaHint}</p> : null}
      {lrcErr ? <p className="post-toc__lyrics-err">{lrcErr}</p> : null}
      {!lrcErr && lyricsReady && lrcLines.length === 0 && !plainLyrics ? (
        <p className="post-toc__lyrics-empty">暂无歌词</p>
      ) : null}
      {!lrcErr && !lyricsReady && lrcLines.length === 0 && !plainLyrics ? (
        <p className="post-toc__lyrics-empty">正在加载歌词…</p>
      ) : null}
      {plainLyrics && !lrcLines.length ? <pre className="post-toc__lyrics-plain">{plainLyrics}</pre> : null}
      {lrcLines.map((line, i) => (
        <p
          key={`${line.time}-${i}`}
          ref={(el) => {
            lineRefs.current[i] = el;
          }}
          className={`post-toc__lyrics-line${i === activeLineIndex ? " post-toc__lyrics-line--active" : ""}`}
        >
          {line.text}
        </p>
      ))}
    </div>
  );
}
