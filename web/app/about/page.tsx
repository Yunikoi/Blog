import { getSiteInfo } from "@/lib/posts";

export default async function AboutPage() {
  const { blogName, blogDescription } = await getSiteInfo();
  return (
    <div className="wrap">
      <h1>关于</h1>
      <p className="lead">{blogName}</p>
      <p className="about-description">
        {blogDescription ||
          "暂无介绍：在仓库根目录的 content/manifest.json 里填写 blogDescription（可多行）；站名来自同文件的 blogName。"}
      </p>
    </div>
  );
}
