import fs from "fs";
import path from "path";

/** 支持从 `web/` 或仓库根目录运行 Next（cwd 不同） */
export function getContentDir(): string {
  const candidates = [path.join(process.cwd(), "content"), path.join(process.cwd(), "..", "content")];
  for (const c of candidates) {
    try {
      if (fs.existsSync(path.join(c, "manifest.json"))) return c;
    } catch {
      /* ignore */
    }
  }
  return candidates[0];
}
