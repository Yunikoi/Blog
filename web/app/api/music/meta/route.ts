import path from "path";
import { parseFile } from "music-metadata";
import { resolveMusicFilePath } from "@/lib/music-public";

async function fetchItunesArtwork(artist: string, title: string): Promise<string | null> {
  const q = [artist, title].filter(Boolean).join(" ").trim();
  if (!q) return null;
  try {
    const res = await fetch(
      `https://itunes.apple.com/search?term=${encodeURIComponent(q)}&limit=1&media=music`,
      { next: { revalidate: 86400 } }
    );
    if (!res.ok) return null;
    const j = (await res.json()) as { results?: { artworkUrl100?: string }[] };
    const url = j.results?.[0]?.artworkUrl100;
    if (!url) return null;
    return url.replace(/100x100bb\.jpg/i, "600x600bb.jpg");
  } catch {
    return null;
  }
}

/** LRCLIB 开源歌词库（无需 key） */
async function fetchLrclibLyrics(artist: string, title: string, durationSec?: number): Promise<string | null> {
  const params = new URLSearchParams();
  if (artist) params.set("artist_name", artist);
  if (title) params.set("track_name", title);
  if (durationSec != null && durationSec > 0) params.set("duration", String(Math.round(durationSec)));

  const getUrl = `https://lrclib.net/api/get?${params.toString()}`;
  let res = await fetch(getUrl, { next: { revalidate: 3600 } });
  if (res.ok) {
    const j = (await res.json()) as { syncedLyrics?: string; plainLyrics?: string };
    if (j.syncedLyrics && j.syncedLyrics.trim()) return j.syncedLyrics;
    if (j.plainLyrics && j.plainLyrics.trim()) return j.plainLyrics;
  }

  const q = [artist, title].filter(Boolean).join(" ");
  if (!q.trim()) return null;
  res = await fetch(`https://lrclib.net/api/search?q=${encodeURIComponent(q)}&limit=3`, { next: { revalidate: 3600 } });
  if (!res.ok) return null;
  const arr = (await res.json()) as { syncedLyrics?: string; plainLyrics?: string }[];
  if (!Array.isArray(arr) || !arr.length) return null;
  const pick = arr[0];
  if (pick.syncedLyrics?.trim()) return pick.syncedLyrics;
  if (pick.plainLyrics?.trim()) return pick.plainLyrics;
  return null;
}

export async function GET(req: Request) {
  const url = new URL(req.url);
  const f = url.searchParams.get("f");
  if (!f) return Response.json({ error: "missing f" }, { status: 400 });

  const full = await resolveMusicFilePath(f);
  if (!full) return Response.json({ error: "not found" }, { status: 404 });

  try {
    const meta = await parseFile(full);
    const artist = meta.common.artist || meta.common.artists?.[0] || "";
    const title = meta.common.title || path.basename(f, path.extname(f));
    const durationSec = typeof meta.format.duration === "number" ? meta.format.duration : undefined;

    let coverDataUrl: string | undefined;
    const pic = meta.common.picture?.[0];
    if (pic?.data?.length) {
      const mime = pic.format || "image/jpeg";
      const buf = Buffer.from(pic.data);
      coverDataUrl = `data:${mime};base64,${buf.toString("base64")}`;
    }
    if (!coverDataUrl) {
      const remote = await fetchItunesArtwork(artist, title);
      if (remote) coverDataUrl = remote;
    }

    let synced: string | null = null;
    let plain: string | null = null;
    try {
      const lr = await fetchLrclibLyrics(artist, title, durationSec);
      if (lr) {
        if (lr.includes("[") && /\[\d{2}:\d{2}/.test(lr)) synced = lr;
        else plain = lr;
      }
    } catch {
      /* ignore */
    }

    return Response.json({
      artist: artist || null,
      title,
      coverDataUrl: coverDataUrl || null,
      lrcText: synced,
      plainLyrics: plain,
    });
  } catch (e) {
    console.error("[music/meta]", e);
    return Response.json({ error: "parse failed" }, { status: 500 });
  }
}
