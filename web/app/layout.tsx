import type { Metadata } from "next";
import "./globals.css";
import SiteHeader from "@/components/SiteHeader";

export const dynamic = "force-dynamic";

export async function generateMetadata(): Promise<Metadata> {
  const { getSiteInfo } = await import("@/lib/posts");
  const { blogName, blogDescription } = await getSiteInfo();
  return {
    title: { default: blogName, template: `%s · ${blogName}` },
    description: blogDescription || undefined,
  };
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body className="body">
        <SiteHeader />
        <main className="main-shell">{children}</main>
      </body>
    </html>
  );
}
