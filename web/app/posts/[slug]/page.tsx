import Link from "next/link";
import { notFound } from "next/navigation";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { getPost, getSiteInfo } from "@/lib/posts";

export const dynamic = "force-dynamic";

type Props = { params: { slug: string } };

export async function generateMetadata({ params }: Props) {
  const post = await getPost(params.slug);
  if (!post) return { title: "未找到" };
  const { blogName } = await getSiteInfo();
  return { title: `${post.title} · ${blogName}` };
}

export default async function PostPage({ params }: Props) {
  const post = await getPost(params.slug);
  if (!post) notFound();

  const { blogName } = await getSiteInfo();

  return (
    <div className="wrap">
      <nav className="nav">
        <Link href="/">← {blogName}</Link>
      </nav>
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
