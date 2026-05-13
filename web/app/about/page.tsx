import { getSiteInfo } from "@/lib/posts";

export const dynamic = "force-dynamic";

export default async function AboutPage() {
  const { blogName, blogDescription } = await getSiteInfo();
  return (
    <div className="wrap">
      <h1>关于</h1>
      <p className="lead">{blogName}</p>
      <p style={{ color: "var(--muted)" }}>{blogDescription || "暂无介绍，可在 content/manifest.json 中填写 blogDescription。"}</p>
    </div>
  );
}
