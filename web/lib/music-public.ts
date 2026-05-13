import fs from "fs/promises";
import path from "path";

const MUSIC_DIR = path.join(process.cwd(), "public", "music");

export type PublicMusicTrack = {
  /** URL 路径，已编码文件名 */
  src: string;
  /** 展示用（去掉 .mp3） */
  title: string;
  /** 原始文件名，用于 API 查询歌词 */
  filename: string;
};

function safeMusicFilename(name: string): boolean {
  if (!name || name.length > 200) return false;
  if (name.includes("..") || name.includes("/") || name.includes("\\")) return false;
  return /\.mp3$/i.test(name);
}

/** 扫描 web/public/music 下 mp3（需提交/部署后线上才可见） */
export async function listPublicMusicTracks(): Promise<PublicMusicTrack[]> {
  let names: string[] = [];
  try {
    names = await fs.readdir(MUSIC_DIR);
  } catch {
    return [];
  }
  const out: PublicMusicTrack[] = [];
  for (const name of names) {
    if (!safeMusicFilename(name)) continue;
    out.push({
      filename: name,
      title: name.replace(/\.mp3$/i, ""),
      src: `/music/${encodeURIComponent(name)}`,
    });
  }
  out.sort((a, b) => a.title.localeCompare(b.title, "zh-CN"));
  return out;
}
