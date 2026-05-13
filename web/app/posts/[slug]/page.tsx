import Link from "next/link";
import { notFound } from "next/navigation";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
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

  return (
    <div className="wrap">
      <p className="meta">
        <Link href="/">← 返回首页</Link>
      </p>
      <article className="prose">
        <h1 style={{ marginTop: 0 }}>{post.title}</h1>
        <p className="meta">
          {post.date || ""}
          {post.tags?.length ? ` · ${post.tags.join(" · ")}` : ""}
        </p>
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{post.content}</ReactMarkdown>
      </article>
    </div>
  );
}
