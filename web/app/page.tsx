import { getSiteInfo, listPosts } from "@/lib/posts";
import { groupPostsByTags } from "@/lib/post-groups";
import PostListByTag from "@/components/PostListByTag";

export default async function HomePage() {
  const { blogDescription } = await getSiteInfo();
  const posts = await listPosts();
  const groups = groupPostsByTags(posts);

  return (
    <div className="wrap">
      <header className="page-intro">
        {blogDescription ? <p className="lead">{blogDescription}</p> : null}
      </header>
      <h1 className="page-title">文章</h1>
      <p className="meta">按标签分类；点击分类标题可查看该标签下全部文章。</p>
      <PostListByTag groups={groups} />
    </div>
  );
}
