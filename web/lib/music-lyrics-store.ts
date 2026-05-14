"use client";

import { useSyncExternalStore } from "react";
import type { LrcLine } from "@/lib/lrc";

export type MusicLyricsView = {
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

let snapshot: MusicLyricsView = emptyMusicLyricsView;
const listeners = new Set<() => void>();

function viewsEqual(a: MusicLyricsView, b: MusicLyricsView): boolean {
  if (a === b) return true;
  if (a.hasTracks !== b.hasTracks) return false;
  if (a.lyricsReady !== b.lyricsReady) return false;
  if (a.lrcErr !== b.lrcErr) return false;
  if (a.metaHint !== b.metaHint) return false;
  if (a.plainLyrics !== b.plainLyrics) return false;
  if (a.activeLineIndex !== b.activeLineIndex) return false;
  if (a.lrcLines.length !== b.lrcLines.length) return false;
  for (let i = 0; i < a.lrcLines.length; i++) {
    const x = a.lrcLines[i];
    const y = b.lrcLines[i];
    if (x.time !== y.time || x.text !== y.text) return false;
  }
  return true;
}

export function subscribeMusicLyrics(onStoreChange: () => void) {
  listeners.add(onStoreChange);
  return () => listeners.delete(onStoreChange);
}

export function getMusicLyricsView(): MusicLyricsView {
  return snapshot;
}

/** 仅在实际变化时通知订阅者，避免整站随播放进度重渲染导致 Link 失效 */
export function setMusicLyricsView(next: MusicLyricsView) {
  if (viewsEqual(snapshot, next)) return;
  snapshot = next;
  listeners.forEach((fn) => fn());
}

export function useMusicLyricsView(): MusicLyricsView {
  return useSyncExternalStore(subscribeMusicLyrics, getMusicLyricsView, getMusicLyricsView);
}
