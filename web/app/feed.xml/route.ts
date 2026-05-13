import { listPosts, getSiteInfo, publicSiteOrigin } from "@/lib/posts";

export const dynamic = "force-dynamic";

function xmlEscape(s: string) {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function rssPubDate(dateStr: string | undefined): string {
  if (!dateStr) return "";
  const s = String(dateStr).trim();
  const d = s.includes("T") ? new Date(s) : new Date(s.slice(0, 10) + "T12:00:00Z");
  if (Number.isNaN(d.getTime())) return "";
  return `<pubDate>${d.toUTCString()}</pubDate>`;
}

export async function GET() {
  try {
    const posts = await listPosts();
    const { blogName, blogDescription } = await getSiteInfo();
    const origin = publicSiteOrigin();

    const items = posts
      .map((p) => {
        const link = `${origin}/posts/${encodeURIComponent(p.slug)}`;
        const desc = xmlEscape((p.excerpt || "").slice(0, 500));
        return `
    <item>
      <title>${xmlEscape(p.title)}</title>
      <link>${xmlEscape(link)}</link>
      <guid>${xmlEscape(link)}</guid>
      <description>${desc}</description>
      ${rssPubDate(p.date)}
    </item>`;
      })
      .join("");

    const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>${xmlEscape(blogName)}</title>
    <link>${xmlEscape(origin + "/")}</link>
    <description>${xmlEscape(blogDescription || blogName)}</description>
    <language>zh-CN</language>
    ${items}
  </channel>
</rss>`;

    return new Response(xml, {
      headers: {
        "Content-Type": "application/rss+xml; charset=utf-8",
        "Cache-Control": "no-store",
      },
    });
  } catch (e) {
    console.error("[feed.xml]", e);
    return new Response("RSS 生成失败", { status: 500 });
  }
}
