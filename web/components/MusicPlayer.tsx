"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { activeLrcIndex, parseLrc, type LrcLine } from "@/lib/lrc";
import type { MusicTrack } from "@/lib/site";

type LocalTrack = {
  id: string;
  title: string;
  src: string;
  lrcText?: string;
};

type Props = {
  /** 为 true 时才把 site.json 里的歌单并入播放器 */
  useServerPlaylist: boolean;
  playlist: MusicTrack[];
};

function readTextFile(f: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onload = () => resolve(String(r.result || ""));
    r.onerror = () => reject(new Error("read"));
    r.readAsText(f, "utf-8");
  });
}

function stem(name: string): string {
  return name.replace(/\.[^.\\/]+$/i, "");
}

export default function MusicPlayer({ useServerPlaylist, playlist }: Props) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const lineRefs = useRef<(HTMLParagraphElement | null)[]>([]);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const [localTracks, setLocalTracks] = useState<LocalTrack[]>([]);
  const [idx, setIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [t, setT] = useState(0);
  const [lyricsOpen, setLyricsOpen] = useState(true);
  const [lrcLines, setLrcLines] = useState<LrcLine[]>([]);
  const [lrcErr, setLrcErr] = useState<string | null>(null);

  const serverList = useServerPlaylist
    ? Array.isArray(playlist)
      ? playlist.filter((x) => x.src)
      : []
    : [];

  const merged: { title: string; src: string; lrcText?: string; lrcUrl?: string; localId?: string }[] = [
    ...serverList.map((x) => ({
      title: x.title,
      src: x.src,
      lrcText: x.lrc,
      lrcUrl: x.lrcUrl,
    })),
    ...localTracks.map((x) => ({
      title: x.title,
      src: x.src,
      lrcText: x.lrcText,
      localId: x.id,
    })),
  ];

  const track = merged[idx];
  const src = track?.src ?? "";

  useEffect(() => {
    lineRefs.current = [];
  }, [lrcLines]);

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
  }, [src, idx]);

  useEffect(() => {
    let cancelled = false;
    async function loadLrc() {
      if (!track) return;
      if (track.lrcText) {
        setLrcLines(parseLrc(track.lrcText));
        return;
      }
      if (track.lrcUrl) {
        try {
          const res = await fetch(track.lrcUrl, { credentials: "omit" });
          if (!res.ok) throw new Error(String(res.status));
          const text = await res.text();
          if (!cancelled) setLrcLines(parseLrc(text));
        } catch {
          if (!cancelled) {
            setLrcErr("歌词加载失败（优先把 .lrc 放到 public 同域，或内联到 site.json 的 lrc 字段）");
            setLrcLines([]);
          }
        }
        return;
      }
      setLrcLines([]);
    }
    void loadLrc();
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

  useEffect(() => {
    return () => {
      for (const x of localTracks) {
        if (x.src.startsWith("blob:")) URL.revokeObjectURL(x.src);
      }
    };
  }, [localTracks]);

  const removeLocal = (id: string) => {
    setLocalTracks((prev) => {
      const hit = prev.find((x) => x.id === id);
      if (hit?.src.startsWith("blob:")) URL.revokeObjectURL(hit.src);
      return prev.filter((x) => x.id !== id);
    });
    setIdx(0);
  };

  const onImportFiles = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const list = e.target.files;
    if (!list?.length) return;
    const arr = [...list];
    const lrcByStem = new Map<string, string>();
    for (const f of arr) {
      if (/\.lrc$/i.test(f.name)) {
        try {
          lrcByStem.set(stem(f.name), await readTextFile(f));
        } catch {
          setErr("无法读取某个 .lrc 文件");
        }
      }
    }
    const audios = arr.filter(
      (f) => f.type.startsWith("audio/") || /\.(mp3|m4a|wav|ogg|flac|aac|opus)$/i.test(f.name)
    );
    const added: LocalTrack[] = [];
    for (const a of audios) {
      const s = stem(a.name);
      const url = URL.createObjectURL(a);
      added.push({
        id: `local-${Date.now()}-${s}-${Math.random().toString(36).slice(2, 8)}`,
        title: s,
        src: url,
        lrcText: lrcByStem.get(s),
      });
    }
    if (added.length) {
      setLocalTracks((prev) => {
        const next = [...prev, ...added];
        queueMicrotask(() => setIdx(serverList.length + next.length - 1));
        return next;
      });
    }
    e.target.value = "";
  };

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
          setErr("无法播放（请换浏览器支持的格式，或检查文件是否损坏）");
          setPlaying(false);
        }
      );
    }
  };

  const next = () => setIdx((i) => (merged.length ? (i + 1) % merged.length : 0));
  const prev = () => setIdx((i) => (merged.length ? (i - 1 + merged.length) % merged.length : 0));

  const isLocalRow = (i: number) => i >= serverList.length;
  const localIdAt = (i: number) => localTracks[i - serverList.length]?.id;

  const hasAnyTrack = merged.length > 0;

  return (
    <div className="music-player" role="region" aria-label="音乐播放器">
      <audio ref={audioRef} preload="metadata" onTimeUpdate={onTimeUpdate} onEnded={() => next()} />

      {hasAnyTrack ? (
        <div className={`music-player__lyrics-wrap${lyricsOpen ? " is-open" : ""}`}>
          <button
            type="button"
            className="music-player__lyrics-toggle"
            onClick={() => setLyricsOpen((o) => !o)}
            aria-expanded={lyricsOpen}
          >
            歌词 {lyricsOpen ? "▼" : "▶"}
          </button>
          {lyricsOpen ? (
            <div className="music-player__lyrics" role="log" aria-live="polite">
              {lrcErr ? <p className="music-player__lyrics-err">{lrcErr}</p> : null}
              {!lrcErr && lrcLines.length === 0 ? (
                <p className="music-player__lyrics-empty">
                  本首暂无歌词。可把 <code>.lrc</code> 放到 <code>web/public/music/</code> 并在 site.json 写{" "}
                  <code>lrcUrl: &quot;/music/歌名.lrc&quot;</code>，或导入时同时选中同名 <code>.lrc</code> 与音频。
                </p>
              ) : (
                lrcLines.map((line, i) => (
                  <p
                    key={`${line.time}-${i}`}
                    ref={(el) => {
                      lineRefs.current[i] = el;
                    }}
                    className={`music-player__lyrics-line${i === activeIdx ? " music-player__lyrics-line--active" : ""}`}
                  >
                    {line.text}
                  </p>
                ))
              )}
            </div>
          ) : null}
        </div>
      ) : null}

      <div className="music-player__inner">
        <div className="music-player__meta">
          <span className="music-player__title">{track?.title || "未选择曲目"}</span>
          {hasAnyTrack ? (
            <span className="music-player__idx">
              {idx + 1} / {merged.length}
            </span>
          ) : (
            <span className="music-player__idx music-player__idx--hint">使用「导入音乐」或开启 site.json 中的歌单</span>
          )}
        </div>
        <div className="music-player__controls">
          <input
            ref={fileInputRef}
            type="file"
            className="music-player__file"
            multiple
            accept="audio/*,.lrc,audio/mpeg,audio/mp4"
            onChange={onImportFiles}
          />
          <button type="button" className="music-player__btn-import" onClick={() => fileInputRef.current?.click()}>
            导入音乐
          </button>
          <button type="button" onClick={prev} aria-label="上一首" disabled={!hasAnyTrack}>
            ‹
          </button>
          <button type="button" onClick={playPause} aria-label={playing ? "暂停" : "播放"} disabled={!src}>
            {playing ? "‖" : "▶"}
          </button>
          <button type="button" onClick={next} aria-label="下一首" disabled={!hasAnyTrack}>
            ›
          </button>
        </div>
        {hasAnyTrack && isLocalRow(idx) ? (
          <button type="button" className="music-player__btn-remove" onClick={() => localIdAt(idx) && removeLocal(localIdAt(idx)!)}>
            移除本首
          </button>
        ) : null}
        {err ? <p className="music-player__err">{err}</p> : null}
      </div>
    </div>
  );
}
