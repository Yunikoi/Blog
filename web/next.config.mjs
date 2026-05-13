import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    // 让 Vercel 打包时把上一级仓库里的 content/ 一并打进 Serverless，避免运行时读不到 Markdown
    outputFileTracingRoot: path.join(__dirname, ".."),
  },
};

export default nextConfig;
