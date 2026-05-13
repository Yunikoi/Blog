"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { activeLrcIndex, parseLrc, type LrcLine } from "@/lib/lrc";
import type { MusicTrack } from "@/lib/site";
import type { PublicMusicTrack } from "@/lib/music-public";

type Merged = {
  title: string;
  src: string;
  filename?: string;
  lrcText?: string;
  lrcUrl?: string;
};

type Props = {
  useServerPlaylist: boolean;
  playlist: MusicTrack[];
  publicTracks: PublicMusicTrack[];
};

export default function MusicPlayer({ useServerPlaylist, playlist, publicTracks }: Props) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const lineRefs = useRef<(HTMLParagraphElement | null)[]>([]);

  const [idx, setIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [t, setT] = useState(0);
  const [lyricsOpen, setLyricsOpen] = useState(true);
  const [lrcLines, setLrcLines] = useState<LrcLine[]>([]);
  const [plainLyrics, setPlainLyrics] = useState<string | null>(null);
  const [lrcErr, setLrcErr] = useState<string | null>(null);
  const [coverUrl, setCoverUrl] = useState<string | null>(null);
  const [metaHint, setMetaHint] = useState<string | null>(null);
  const [lyricsReady, setLyricsReady] = useState(false);

  const serverList = useServerPlaylist
    ? Array.isArray(playlist)
      ? playlist.filter((x) => x.src)
      : []
    : [];

  const merged: Merged[] = [
    ...publicTracks.map((p) => ({
      title: p.title,
      src: p.src,
      filename: p.filename,
    })),
    ...serverList.map((x) => ({
      title: x.title,
      src: x.src,
      lrcText: x.lrc,
      lrcUrl: x.lrcUrl,
    })),
  ];

  const track = merged[idx];
  const src = track?.src ?? "";

  useEffect(() => {
    lineRefs.current = [];
  }, [lrcLines, plainLyrics]);

  useEffect(() => {
    const el = audioRef.current;
    if (!el || !src) return;
    el.pause();
    setPlaying(false);
    el.src = src;
    el.load();
    setErr(null);
    setT(0);
    setLrcErr(null);
    setLrcLines([]);
    setPlainLyrics(null);
    setCoverUrl(null);
    setMetaHint(null);
    setLyricsReady(false);
  }, [src, idx]);

  useEffect(() => {
    let cancelled = false;
    async function load() {
      if (!track) {
        setLyricsReady(true);
        return;
      }
      if (track.lrcText) {
        const lines = parseLrc(track.lrcText);
        if (lines.length) setLrcLines(lines);
        else if (track.lrcText.trim()) setPlainLyrics(track.lrcText.trim());
        setLyricsReady(true);
        return;
      }
      if (track.lrcUrl) {
        try {
          const res = await fetch(track.lrcUrl, { credentials: "omit" });
          if (!res.ok) throw new Error(String(res.status));
          const text = await res.text();
          if (cancelled) return;
          const lines = parseLrc(text);
          if (lines.length) setLrcLines(lines);
          else if (text.trim()) setPlainLyrics(text.trim());
        } catch {
          if (!cancelled) setLrcErr("歌词文件加载失败");
        } finally {
          if (!cancelled) setLyricsReady(true);
        }
        return;
      }
      if (track.filename) {
        try {
          const res = await fetch(`/api/music/meta?f=${encodeURIComponent(track.filename)}`);
          if (!res.ok) throw new Error(String(res.status));
          const j = (await res.json()) as {
            artist?: string | null;
            title?: string;
            coverDataUrl?: string | null;
            lrcText?: string | null;
            plainLyrics?: string | null;
          };
          if (cancelled) return;
          if (j.coverDataUrl) setCoverUrl(j.coverDataUrl);
          if (j.artist || j.title) setMetaHint([j.artist, j.title].filter(Boolean).join(" · "));
          if (j.lrcText?.trim()) {
            const lines = parseLrc(j.lrcText);
            if (lines.length) setLrcLines(lines);
            else if (j.lrcText.trim()) setPlainLyrics(j.lrcText.trim());
          } else if (j.plainLyrics?.trim()) {
            setPlainLyrics(j.plainLyrics.trim());
          }
        } catch {
          if (!cancelled) setLrcErr("无法获取歌词（请检查网络或稍后重试）");
        } finally {
          if (!cancelled) setLyricsReady(true);
        }
      } else {
        setLyricsReady(true);
      }
    }
    void load();
    return () => {
      cancelled = true;
    };
  }, [track]);

  const onTimeUpdate = useCallback(() => {
    const el = audioRef.current;
    if (!el) return;
    setT(el.currentTime);
  }, []);

  const activeIdx = lrcLines.length ? activeLrcIndex(lrcLines, t) : -1;

  useEffect(() => {
    if (activeIdx < 0) return;
    const el = lineRefs.current[activeIdx];
    el?.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }, [activeIdx]);

  const hasAnyTrack = merged.length > 0;

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
          setErr("无法播放该音频文件");
          setPlaying(false);
        }
      );
    }
  };

  const next = () => setIdx((i) => (merged.length ? (i + 1) % merged.length : 0));
  const prev = () => setIdx((i) => (merged.length ? (i - 1 + merged.length) % merged.length : 0));

  if (!hasAnyTrack) {
    return (
      <div className="music-player music-player--empty" role="region" aria-label="音乐播放器">
        <div className="music-player__inner">
          <p className="music-player__empty-hint">
            将 <strong>.mp3</strong> 放入仓库 <code>web/public/music/</code> 并重新部署；播放器会自动扫描并尝试从 LRCLIB 匹配歌词、读取文件内嵌封面。
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="music-player" role="region" aria-label="音乐播放器">
      <audio ref={audioRef} preload="metadata" onTimeUpdate={onTimeUpdate} onEnded={() => next()} />

      <div className={`music-player__lyrics-wrap${lyricsOpen ? " is-open" : ""}`}>
        <button
          type="button"
          className="music-player__lyrics-toggle"
          onClick={() => setLyricsOpen((o) => !o)}
          aria-expanded={lyricsOpen}
        >
          歌词 / 封面 {lyricsOpen ? "▼" : "▶"}
        </button>
        {lyricsOpen ? (
          <div className="music-player__lyrics-panel">
            {coverUrl ? (
              <div className="music-player__cover-wrap">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={coverUrl} alt="" className="music-player__cover" width={120} height={120} />
              </div>
            ) : null}
            <div className="music-player__lyrics" role="log" aria-live="polite">
              {metaHint ? <p className="music-player__meta-hint">{metaHint}</p> : null}
              {lrcErr ? <p className="music-player__lyrics-err">{lrcErr}</p> : null}
              {!lrcErr && lyricsReady && lrcLines.length === 0 && !plainLyrics ? (
                <p className="music-player__lyrics-empty">暂无歌词（可检查 MP3 内嵌歌手/歌名是否便于匹配）</p>
              ) : null}
              {!lrcErr && !lyricsReady && lrcLines.length === 0 && !plainLyrics ? (
                <p className="music-player__lyrics-empty">正在加载歌词…</p>
              ) : null}
              {plainLyrics && !lrcLines.length ? <pre className="music-player__plain">{plainLyrics}</pre> : null}
              {lrcLines.map((line, i) => (
                <p
                  key={`${line.time}-${i}`}
                  ref={(el) => {
                    lineRefs.current[i] = el;
                  }}
                  className={`music-player__lyrics-line${i === activeIdx ? " music-player__lyrics-line--active" : ""}`}
                >
                  {line.text}
                </p>
              ))}
            </div>
          </div>
        ) : null}
      </div>

      <div className="music-player__inner">
        {coverUrl && !lyricsOpen ? (
          <div className="music-player__thumb">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={coverUrl} alt="" width={40} height={40} />
          </div>
        ) : null}
        <div className="music-player__meta">
          <span className="music-player__title">{track?.title || "—"}</span>
          <span className="music-player__idx">
            {idx + 1} / {merged.length}
          </span>
        </div>
        <div className="music-player__controls">
          <button type="button" onClick={prev} aria-label="上一首">
            ‹
          </button>
          <button type="button" onClick={playPause} aria-label={playing ? "暂停" : "播放"} disabled={!src}>
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
