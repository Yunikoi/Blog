import path from "path";
import fs from "fs";

/**
 * 优先使用 web/content（由 prebuild/predev 从仓库根同步），否则回退到 ../content。
 */
export function getContentDir(): string {
  const cwd = process.cwd();
  const candidates = [
    path.join(cwd, "content"),
    path.join(cwd, "..", "content"),
  ];
  for (const c of candidates) {
    try {
      if (fs.existsSync(path.join(c, "manifest.json"))) return c;
    } catch {
      /* ignore */
    }
  }
  return candidates[0];
}
