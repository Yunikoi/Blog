/**
 * 将仓库根目录的 content/ 同步到 web/content/，便于 Vercel 等环境打包进 Serverless。
 * 开发时以仓库根 content 为准；请勿在 web/content 里长期手写（会被覆盖）。
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const webRoot = path.join(__dirname, "..");
const src = path.join(webRoot, "..", "content");
const dest = path.join(webRoot, "content");
const marker = path.join(src, "manifest.json");

if (!fs.existsSync(marker)) {
  console.warn("[sync-content] 未找到 ../content/manifest.json，跳过同步（若仅部署 web 子目录请确保仓库含 content）。");
  process.exit(0);
}

fs.rmSync(dest, { recursive: true, force: true });
fs.cpSync(src, dest, { recursive: true });
console.log("[sync-content] 已同步到 web/content");
