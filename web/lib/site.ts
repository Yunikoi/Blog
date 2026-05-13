import fs from "fs/promises";
import path from "path";
import { getContentDir } from "@/lib/content-dir";

export type SocialLink = { label: string; url: string };

export type SiteProfile = {
  name?: string;
  bio?: string;
  avatar?: string;
  links?: SocialLink[];
};

export type MusicTrack = {
  title: string;
  /** 音频直链，或本站 public 下路径如 /music/a.mp3 */
  src: string;
  /** 内联 LRC 全文 */
  lrc?: string;
  /** 与音频同域或可跨域访问的 .lrc 地址 */
  lrcUrl?: string;
};

export type SiteExtra = {
  profile: SiteProfile;
  music: {
    enabled: boolean;
    playlist: MusicTrack[];
  };
};

const defaultExtra: SiteExtra = {
  profile: { name: "", bio: "", avatar: "", links: [] },
  music: { enabled: false, playlist: [] },
};

export async function getSiteExtra(): Promise<SiteExtra> {
  const file = path.join(getContentDir(), "site.json");
  try {
    const raw = await fs.readFile(file, "utf8");
    const j = JSON.parse(raw) as Partial<SiteExtra>;
    return {
      profile: {
        name: typeof j.profile?.name === "string" ? j.profile.name : "",
        bio: typeof j.profile?.bio === "string" ? j.profile.bio : "",
        avatar: typeof j.profile?.avatar === "string" ? j.profile.avatar : "",
        links: Array.isArray(j.profile?.links)
          ? j.profile!.links!.filter(
              (x): x is SocialLink =>
                x && typeof (x as SocialLink).label === "string" && typeof (x as SocialLink).url === "string"
            )
          : [],
      },
      music: {
        enabled: !!j.music?.enabled,
        playlist: Array.isArray(j.music?.playlist)
          ? j.music!.playlist!.filter((x): x is MusicTrack => {
              if (!x || typeof (x as MusicTrack).title !== "string" || typeof (x as MusicTrack).src !== "string")
                return false;
              const m = x as MusicTrack;
              if (m.lrc !== undefined && typeof m.lrc !== "string") return false;
              if (m.lrcUrl !== undefined && typeof m.lrcUrl !== "string") return false;
              return true;
            })
          : [],
      },
    };
  } catch {
    return defaultExtra;
  }
}
