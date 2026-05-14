"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { activeLrcIndex, parseLrc, type LrcLine } from "@/lib/lrc";
import type { MusicTrack } from "@/lib/site";
import type { PublicMusicTrack } from "@/lib/music-public";
import { emptyMusicLyricsView, useMusicLyrics } from "@/components/MusicLyricsProvider";

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
  /** 服务端扫描结果；若为空客户端会请求 /api/music/tracks 兜底（部署未带上 mp3 时仍可能为空） */
  publicTracks?: PublicMusicTrack[];
};

export default function MusicPlayer({ useServerPlaylist, playlist, publicTracks = [] }: Props) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const lyricsCtx = useMusicLyrics();

  const [remoteLibrary, setRemoteLibrary] = useState<PublicMusicTrack[] | null>(null);

  const library = publicTracks.length > 0 ? publicTracks : remoteLibrary ?? [];

  useEffect(() => {
    if (publicTracks.length > 0) {
      setRemoteLibrary(null);
      return;
    }
    let cancelled = false;
    void fetch("/api/music/tracks")
      .then((r) => r.json())
      .then((t: PublicMusicTrack[]) => {
        if (cancelled || !Array.isArray(t) || !t.length) return;
        setRemoteLibrary(t);
      })
      .catch(() => {});
    return () => {
      cancelled = true;
    };
  }, [publicTracks.length]);

  const [idx, setIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [t, setT] = useState(0);
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
    ...library.map((p) => ({
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
  /** 应用内曲目对象每轮渲染都是新引用，勿把 `track` 放进 effect 依赖，否则会无休止请求 meta */
  const lyricsFetchKey = track
    ? `${idx}\0${src}\0${track.filename ?? ""}\0${track.lrcUrl ?? ""}\0${track.lrcText ?? ""}`
    : "";

  const mergedRef = useRef(merged);
  mergedRef.current = merged;

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
    const tr = mergedRef.current[idx];

    async function load() {
      if (!tr) {
        setLyricsReady(true);
        return;
      }
      if (tr.lrcText) {
        const lines = parseLrc(tr.lrcText);
        if (lines.length) setLrcLines(lines);
        else if (tr.lrcText.trim()) setPlainLyrics(tr.lrcText.trim());
        setLyricsReady(true);
        return;
      }
      if (tr.lrcUrl) {
        try {
          const res = await fetch(tr.lrcUrl, { credentials: "omit" });
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
      if (tr.filename) {
        try {
          const res = await fetch(`/api/music/meta?f=${encodeURIComponent(tr.filename)}`);
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
  }, [lyricsFetchKey]);

  const onTimeUpdate = useCallback(() => {
    const el = audioRef.current;
    if (!el) return;
    setT(el.currentTime);
  }, []);

  const activeIdx = lrcLines.length ? activeLrcIndex(lrcLines, t) : -1;

  useEffect(() => {
    if (!lyricsCtx) return;
    if (!merged.length) {
      lyricsCtx.setLyricsView(emptyMusicLyricsView);
      return;
    }
    lyricsCtx.setLyricsView({
      hasTracks: true,
      lrcLines,
      plainLyrics,
      activeLineIndex: activeIdx,
      lrcErr,
      lyricsReady,
      metaHint,
    });
  }, [lyricsCtx, merged.length, lrcLines, plainLyrics, activeIdx, lrcErr, lyricsReady, metaHint]);

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
            将 <strong>.mp3</strong> 放入 <code>web/public/music/</code> 并提交部署；本地在 <code>web</code> 目录运行 <code>npm run dev</code>。若仍无列表，请打开开发者工具看 <code>/api/music/tracks</code> 是否返回 JSON（部署环境若未包含 mp3 文件则为空）。
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="music-player" role="region" aria-label="音乐播放器">
      <audio
        ref={audioRef}
        preload="metadata"
        onTimeUpdate={onTimeUpdate}
        onEnded={() => next()}
        onError={() => {
          setPlaying(false);
          setErr("无法播放该音频文件");
        }}
      />

      <div className="music-player__inner">
        {coverUrl ? (
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
