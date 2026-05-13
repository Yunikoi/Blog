import type { SiteProfile } from "@/lib/site";

export default function SiteProfile({ profile }: { profile: SiteProfile }) {
  const name = profile.name?.trim();
  const bio = profile.bio?.trim();
  const avatar = profile.avatar?.trim();
  const links = profile.links || [];

  if (!name && !bio && !avatar && links.length === 0) {
    return (
      <section className="site-profile site-profile--empty">
        <p className="site-profile__hint">
          在 <code>content/site.json</code> 的 <code>profile.avatar</code> 填图片地址：可用图床 URL，或把图片放在{" "}
          <code>web/public/</code> 下并填 <code>/文件名.jpg</code>（例如 <code>/avatar.jpg</code>）。
        </p>
      </section>
    );
  }

  return (
    <section className="site-profile" aria-label="个人资料">
      {avatar ? (
        <img
          className="site-profile__avatar"
          src={avatar}
          alt=""
          width={72}
          height={72}
          loading="lazy"
          referrerPolicy="no-referrer"
        />
      ) : (
        <div className="site-profile__avatar site-profile__avatar--placeholder" aria-hidden />
      )}
      {name ? <h2 className="site-profile__name">{name}</h2> : null}
      {bio ? <p className="site-profile__bio">{bio}</p> : null}
      {links.length > 0 ? (
        <ul className="site-profile__links">
          {links.map((l) => (
            <li key={l.url}>
              <a href={l.url} target="_blank" rel="noopener noreferrer">
                {l.label}
              </a>
            </li>
          ))}
        </ul>
      ) : null}
    </section>
  );
}
