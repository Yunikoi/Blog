import { readFile } from "fs/promises";
import type { NextRequest } from "next/server";
import { resolveMusicFilePath } from "@/lib/music-public";

/** 通过 API 提供 mp3，避免 `/music/中文…` 静态路径在部分环境下的编码问题；支持 Range 以便播放器 seek */
export async function GET(req: NextRequest) {
  const raw = req.nextUrl.searchParams.get("f")?.trim() ?? "";
  if (!raw) return new Response("Missing f", { status: 400 });

  const fullPath = await resolveMusicFilePath(raw);
  if (!fullPath) return new Response("Not found", { status: 404 });

  const buffer = await readFile(fullPath);
  const size = buffer.length;

  const range = req.headers.get("range");
  if (!range) {
    return new Response(buffer, {
      headers: {
        "Content-Type": "audio/mpeg",
        "Content-Length": String(size),
        "Accept-Ranges": "bytes",
        "Cache-Control": "public, max-age=86400",
      },
    });
  }

  const m = /^bytes=(\d*)-(\d*)$/i.exec(range.trim());
  if (!m) {
    return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${size}` } });
  }

  let start = m[1] === "" ? 0 : parseInt(m[1], 10);
  let end = m[2] === "" ? size - 1 : parseInt(m[2], 10);
  if (Number.isNaN(start) || Number.isNaN(end) || start < 0 || end < start || start >= size) {
    return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${size}` } });
  }
  end = Math.min(end, size - 1);
  const chunk = buffer.subarray(start, end + 1);

  return new Response(chunk, {
    status: 206,
    headers: {
      "Content-Type": "audio/mpeg",
      "Content-Length": String(chunk.length),
      "Content-Range": `bytes ${start}-${end}/${size}`,
      "Accept-Ranges": "bytes",
      "Cache-Control": "public, max-age=86400",
    },
  });
}
