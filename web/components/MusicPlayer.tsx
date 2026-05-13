"use client";

import { useEffect, useRef, useState } from "react";
import type { MusicTrack } from "@/lib/site";

type Props = {
  enabled: boolean;
  playlist: MusicTrack[];
};

export default function MusicPlayer({ enabled, playlist }: Props) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [idx, setIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  const safeList = Array.isArray(playlist) ? playlist.filter((t) => t.src) : [];
  const track = safeList[idx];
  const src = track?.src ?? "";

  useEffect(() => {
    const el = audioRef.current;
    if (!el || !src) return;
    el.pause();
    setPlaying(false);
    el.src = src;
    el.load();
    setErr(null);
  }, [src, idx]);

  if (!enabled || safeList.length === 0) return null;

  const playPause = () => {
    const el = audioRef.current;
    if (!el || !src) return;
    if (playing) {
      el.pause();
      setPlaying(false);
    } else {
      void el.play().then(
        () => setPlaying(true),
        () => {
          setErr("无法播放（需可直链的音频地址，且允许跨域）");
          setPlaying(false);
        }
      );
    }
  };

  const next = () => {
    setIdx((i) => (i + 1) % safeList.length);
  };

  const prev = () => {
    setIdx((i) => (i - 1 + safeList.length) % safeList.length);
  };

  return (
    <div className="music-player" role="region" aria-label="音乐播放器">
      <audio ref={audioRef} preload="none" onEnded={() => next()} />
      <div className="music-player__inner">
        <div className="music-player__meta">
          <span className="music-player__title">{track?.title || "未命名"}</span>
          <span className="music-player__idx">
            {idx + 1} / {safeList.length}
          </span>
        </div>
        <div className="music-player__controls">
          <button type="button" onClick={prev} aria-label="上一首">
            ‹
          </button>
          <button type="button" onClick={playPause} aria-label={playing ? "暂停" : "播放"}>
            {playing ? "‖" : "▶"}
          </button>
          <button type="button" onClick={next} aria-label="下一首">
            ›
          </button>
        </div>
        {err ? <p className="music-player__err">{err}</p> : null}
      </div>
    </div>
  );
}
