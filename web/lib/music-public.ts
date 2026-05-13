import fs from "fs/promises";
import path from "path";

export type PublicMusicTrack = {
  /** URL 路径，已编码文件名 */
  src: string;
  /** 展示用（去掉 .mp3） */
  title: string;
  /** 原始文件名，用于 API 查询歌词 */
  filename: string;
};

/** 兼容从 `web/` 或仓库根目录启动 Next（cwd 不同） */
export function getMusicLibraryDirectories(): string[] {
  const cwd = process.cwd();
  const set = new Set<string>();
  set.add(path.join(cwd, "public", "music"));
  set.add(path.join(cwd, "web", "public", "music"));
  const up = path.dirname(cwd);
  if (path.basename(cwd) === "web") {
    set.add(path.join(up, "web", "public", "music"));
  }
  return [...set];
}

export async function resolveMusicFilePath(filename: string): Promise<string | null> {
  if (!safeMusicFilename(filename)) return null;
  for (const base of getMusicLibraryDirectories()) {
    const full = path.join(base, filename);
    try {
      await fs.access(full);
      return full;
    } catch {
      /* continue */
    }
  }
  return null;
}

function safeMusicFilename(name: string): boolean {
  if (!name || name.length > 200) return false;
  if (name.includes("..") || name.includes("/") || name.includes("\\")) return false;
  return /\.mp3$/i.test(name);
}

/** 扫描所有存在的 `public/music` 目录下的 mp3（合并、按文件名去重） */
export async function listPublicMusicTracks(): Promise<PublicMusicTrack[]> {
  const byFile = new Map<string, PublicMusicTrack>();

  for (const dir of getMusicLibraryDirectories()) {
    let names: string[] = [];
    try {
      names = await fs.readdir(dir);
    } catch {
      continue;
    }
    for (const name of names) {
      if (!safeMusicFilename(name)) continue;
      if (byFile.has(name)) continue;
      byFile.set(name, {
        filename: name,
        title: name.replace(/\.mp3$/i, ""),
        src: `/music/${encodeURIComponent(name)}`,
      });
    }
  }

  return [...byFile.values()].sort((a, b) => a.title.localeCompare(b.title, "zh-CN"));
}
