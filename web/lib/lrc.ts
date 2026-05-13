export type LrcLine = { time: number; text: string };

/** 解析常见 LRC：[mm:ss.xx] 歌词 */
export function parseLrc(raw: string): LrcLine[] {
  const out: LrcLine[] = [];
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed) continue;
    const m = trimmed.match(/^\[(\d{2}):(\d{2})(?:\.(\d{1,3}))?\](.*)$/);
    if (!m) continue;
    const min = Number(m[1]);
    const sec = Number(m[2]);
    const frac = m[3] ? Number(m[3].padEnd(3, "0")) / 1000 : 0;
    const time = min * 60 + sec + frac;
    const text = (m[4] || "").trim();
    if (text) out.push({ time, text });
  }
  out.sort((a, b) => a.time - b.time);
  return out;
}

/** 当前时间所在歌词行（无则 -1） */
export function activeLrcIndex(lines: LrcLine[], t: number): number {
  if (!lines.length) return -1;
  let r = -1;
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].time <= t) r = i;
    else break;
  }
  return r;
}
