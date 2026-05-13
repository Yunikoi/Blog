import type { Metadata } from "next";
import "./globals.css";

export const dynamic = "force-dynamic";

export async function generateMetadata(): Promise<Metadata> {
  const { getSiteInfo } = await import("@/lib/posts");
  const { blogName, blogDescription } = await getSiteInfo();
  return {
    title: blogName,
    description: blogDescription || undefined,
  };
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body className="body">{children}</body>
    </html>
  );
}
