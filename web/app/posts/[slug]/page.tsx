import Link from "next/link";
import { notFound } from "next/navigation";
import ReactMarkdown from "react-markdown";
import rehypeSlug from "rehype-slug";
import remarkGfm from "remark-gfm";
import PostToc from "@/components/PostToc";
import { extractToc } from "@/lib/markdown-toc";
import { getPost } from "@/lib/posts";

type Props = { params: { slug: string } };

export async function generateMetadata({ params }: Props) {
  const post = await getPost(params.slug);
  if (!post) return { title: "未找到" };
  return { title: post.title };
}

export default async function PostPage({ params }: Props) {
  const post = await getPost(params.slug);
  if (!post) notFound();

  const toc = post.showToc ? extractToc(post.content) : [];
  const hasToc = toc.length > 0;

  return (
    <div className={`wrap post-article-wrap${hasToc ? " post-article-wrap--with-toc" : ""}`}>
      <p className="meta">
        <Link href="/">← 返回首页</Link>
      </p>
      <div className={hasToc ? "post-article-grid" : undefined}>
        {hasToc ? <PostToc items={toc} /> : null}
        <article className={`prose post-article-main${hasToc ? "" : " post-article-main--full"}`}>
          <h1 style={{ marginTop: 0 }}>{post.title}</h1>
          <p className="meta">
            {post.column ? <span className="post-col-badge">{post.column}</span> : null}
            {post.column && (post.date || post.tags?.length) ? <span> · </span> : null}
            {post.date || ""}
            {post.tags?.length ? ` · ${post.tags.join(" · ")}` : ""}
          </p>
          <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeSlug]}>
            {post.content}
          </ReactMarkdown>
        </article>
      </div>
    </div>
  );
}
