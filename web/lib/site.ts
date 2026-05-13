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

export type MusicTrack = { title: string; src: string };

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
          ? j.music!.playlist!.filter(
              (x): x is MusicTrack =>
                x && typeof (x as MusicTrack).title === "string" && typeof (x as MusicTrack).src === "string"
            )
          : [],
      },
    };
  } catch {
    return defaultExtra;
  }
}
