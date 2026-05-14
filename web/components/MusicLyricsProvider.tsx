"use client";

import { createContext, useCallback, useContext, useMemo, useState, type ReactNode } from "react";
import type { LrcLine } from "@/lib/lrc";

export type MusicLyricsView = {
  /** 是否有可播放曲目（用于侧栏区分「未配置音乐」与「暂无歌词」） */
  hasTracks: boolean;
  lrcLines: LrcLine[];
  plainLyrics: string | null;
  activeLineIndex: number;
  lrcErr: string | null;
  lyricsReady: boolean;
  metaHint: string | null;
};

export const emptyMusicLyricsView: MusicLyricsView = {
  hasTracks: false,
  lrcLines: [],
  plainLyrics: null,
  activeLineIndex: -1,
  lrcErr: null,
  lyricsReady: false,
  metaHint: null,
};

type Ctx = {
  view: MusicLyricsView;
  setLyricsView: (v: MusicLyricsView) => void;
};

const MusicLyricsContext = createContext<Ctx | undefined>(undefined);

export function useMusicLyrics() {
  return useContext(MusicLyricsContext);
}

export default function MusicLyricsProvider({ children }: { children: ReactNode }) {
  const [view, setView] = useState<MusicLyricsView>(emptyMusicLyricsView);
  const setLyricsView = useCallback((v: MusicLyricsView) => {
    setView(v);
  }, []);
  const value = useMemo(() => ({ view, setLyricsView }), [view, setLyricsView]);
  return <MusicLyricsContext.Provider value={value}>{children}</MusicLyricsContext.Provider>;
}
