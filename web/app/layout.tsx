import type { Metadata } from "next";
import "./globals.css";
import SiteHeader from "@/components/SiteHeader";
import SiteProfile from "@/components/SiteProfile";
import TagTree from "@/components/TagTree";
import { listPublicMusicTracks } from "@/lib/music-public";
import MainShellTransition from "@/components/MainShellTransition";
import LayoutChrome from "@/components/LayoutChrome";
import MusicPlayer from "@/components/MusicPlayer";
import { getSiteExtra } from "@/lib/site";
import { allTags } from "@/lib/posts";
import { buildTagTrie } from "@/lib/tag-tree";

export async function generateMetadata(): Promise<Metadata> {
  const { getSiteInfo } = await import("@/lib/posts");
  const { blogName, blogDescription } = await getSiteInfo();
  return {
    title: { default: blogName, template: `%s · ${blogName}` },
    description: blogDescription || undefined,
  };
}

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const [extra, tags, publicTracks] = await Promise.all([
    getSiteExtra(),
    allTags(),
    listPublicMusicTracks(),
  ]);
  const trie = buildTagTrie(tags);

  return (
    <html lang="zh-CN">
      <body className="body">
        <LayoutChrome>
          <SiteHeader />
          <div className="app-body">
            <MainShellTransition>{children}</MainShellTransition>
            <aside className="site-aside">
              <SiteProfile profile={extra.profile} />
              <TagTree nodes={trie} />
            </aside>
          </div>
        </LayoutChrome>
        <MusicPlayer
          useServerPlaylist={extra.music.enabled}
          playlist={extra.music.playlist}
          publicTracks={publicTracks}
        />
      </body>
    </html>
  );
}
