# Minimal Personal Blog · 极简个人博客

This repository contains **two** ways to use the same Markdown-centric content:

1. **Classic static site** at the repo root: **vanilla HTML, CSS, and JavaScript** with a hash router—matches the default **GitHub Pages** workflow (`.github/workflows/pages.yml` publishes the repo root).
2. **Next.js 14 app** in **`web/`** (App Router): home, posts with optional TOC, tag tree, About page, optional footer music, and synced content from the root **`content/`** folder.

**中文：** 仓库里有两套界面共用 **`content/`** 里的文章与配置：根目录 **纯静态** 博客（适合当前 Pages 工作流），以及 **`web/`** 下的 **Next.js** 阅读站（侧栏简介、标签树、目录与歌词区、路由模糊转场等）。编辑内容请以仓库根目录 **`content/`** 为准；Next 在 `npm run dev` / `npm run build` 时会把其复制到 `web/content/`（勿在 `web/content/` 长期手写）。

---

## Next.js app (`web/`)

### Features

- **Content sync:** `web/scripts/sync-content.mjs` copies `../content` → `web/content` before dev/build (`predev` / `prebuild` in `web/package.json`).
- **Config files (root `content/`):** `manifest.json` — `blogName`, `blogDescription` (About page + site metadata; multi-line OK), `posts[]`; `site.json` — profile (name, bio, avatar path as URL e.g. `/photo.jpg`), links, optional `music` playlist; Markdown bodies in `posts/`.
- **Reading UX:** Sticky TOC on wide screens; current lyric line in the TOC panel when a post has a TOC; soft **blur / fade** transition on the main pane when changing routes (`prefers-reduced-motion` disables it); semi-transparent bottom player.

### Run locally

```bash
cd web
npm install
npm run dev
```

Production: `npm run build` then `npm run start`.

### Deploy note

GitHub Actions in this repo deploys the **static root** to Pages. Host **`web/`** on a Node-compatible platform (e.g. Vercel) if you want the Next app in production.

---

## English

### Features (classic static site at repo root)

- **UI:** Generous whitespace, system / Inter typography, accent color, card list with subtle hover, light / dark theme (auto or manual), smooth theme transitions, `localStorage` for preferences.
- **Routing:** Hash-based SPA (`#/`, `#/post/slug`, `#/about`, `#/tags`, `#/tags/tag`) without full page reloads; ~200 ms view transitions.
- **Article view:** Markdown subset (headings, paragraphs, blockquotes, fenced code with copy, images, links, inline code), reading progress bar, back-to-top, desktop TOC + mobile collapsible TOC, prev/next navigation.
- **GitHub mode:** Load `manifest.json` from `raw.githubusercontent.com`, then fetch each post body from the repo. Falls back to built-in demo posts if the request fails.
- **Settings (footer):** Site title, tagline, theme, GitHub source toggles, optional PAT for private repos (stored in browser only).

### Project layout

```text
Blog/
├── content/                 # Shared: manifest, site profile, posts (source of truth for Next sync)
│   ├── manifest.json      # blogName, blogDescription, posts[]
│   ├── site.json          # Optional: profile + music (used by Next app)
│   └── posts/*.md
├── web/                     # Next.js 14 app
│   ├── app/                 # Routes, layout, globals.css
│   ├── components/
│   ├── lib/
│   ├── public/              # Static assets (e.g. public/music/*.mp3, avatar image)
│   ├── scripts/sync-content.mjs
│   └── package.json
├── index.html               # Classic static shell + settings
├── css/styles.css
├── js/app.js
└── .github/workflows/
    └── pages.yml            # Deploys repo root (static site) to GitHub Pages
```

### Run locally

Open `index.html` in a browser, or serve the folder (recommended):

```bash
npx --yes serve .
```

The **Next.js** reader lives in `web/`; run `cd web && npm install && npm run dev` (see **Next.js app** at the top of this file).

### Use GitHub as the content source

1. Push this repository (or your fork) to GitHub **as a public repo** (or use a PAT for private repos).
2. Edit `content/manifest.json` (post metadata + `file` paths) and add Markdown under `content/posts/`.
3. On the site, open **简易设置** at the bottom: enable **从 GitHub 加载**, enter **username**, **repository**, **branch** (e.g. `main`), and **manifest path** (default `content/manifest.json`), then save.

`manifest.json` shape (valid JSON: commas between every pair; `blogDescription` can use `\n` for line breaks on the Next About page):

```json
{
  "blogName": "Your site name",
  "blogDescription": "First paragraph.\n\nSecond paragraph after a blank line.",
  "posts": [
    {
      "slug": "my-post",
      "title": "Title",
      "date": "2026-05-12",
      "tags": ["Note"],
      "cover": null,
      "excerpt": "Short summary for the list.",
      "file": "content/posts/my-post.md"
    }
  ]
}
```

Each Markdown file may start with optional YAML front matter (`title`, `date`, `tags`, `slug`, `cover`, `excerpt`) followed by the body.

### Deploy to GitHub Pages

1. In the repo on GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Push to `main` or `master`; the workflow in `.github/workflows/pages.yml` publishes the site root.

If the site is served from a **project** URL (`https://<user>.github.io/<repo>/`), relative asset paths (`css/`, `js/`) still work. Use hash routes only; no server rewrite is required.

### Customize without the UI

Before `js/app.js`, you can set:

```html
<script>
  window.blogConfig = window.blogConfig || {};
  window.blogConfig.github = {
    enabled: true,
    user: "YOUR_USERNAME",
    repo: "YOUR_REPO",
    branch: "main",
    manifestPath: "content/manifest.json"
  };
</script>
```

### Browser support

Recent Chrome, Safari, and Firefox (ES2017+ features, `fetch`, `localStorage`).

### License

No license file is bundled; add one in your fork if you need explicit terms.

---

## 中文说明

Next.js 版功能、本地运行与部署说明见上文 **「Next.js app (`web/`)」** 一节；以下为根目录 **静态版** 说明。

### 功能概览（根目录静态站）

- **界面：** 留白、系统字体与 Inter、单一强调色、卡片列表与悬停微动效、浅色 / 深色 / 跟随系统、主题色过渡、`localStorage` 保存偏好。
- **路由：** Hash 单页（`#/`, `#/post/文章slug`, `#/about`, `#/tags`, `#/tags/标签`），无整页刷新，视图切换约 200 ms 淡入淡出。
- **文章页：** 子集 Markdown（标题、段落、引用、代码块与复制、图片、链接、行内代码）、顶部阅读进度、返回顶部、桌面端目录 + 移动端折叠目录、上一篇 / 下一篇。
- **GitHub 模式：** 从 `raw.githubusercontent.com` 拉取 `manifest.json`，再按需拉取各篇 `.md` 正文；拉取失败时自动回退到内置演示文章。
- **简易设置（页脚）：** 站名、一句话介绍、主题、GitHub 源开关与仓库信息；可选 Token（仅保存在本机浏览器，适合私有仓库）。

### 目录结构

见上文 **Project layout**（含 `web/` 与根目录静态文件）。内容统一维护在根目录 **`content/`**；Next 构建前会同步到 `web/content/`。

### 本地运行

直接用浏览器打开 `index.html`，或使用本地静态服务（推荐）：

```bash
npx --yes serve .
```

Next.js 阅读站在 **`web/`** 目录：`cd web`，执行 `npm install` 与 `npm run dev`（详见文件开头的 **Next.js app** 一节）。

### 使用 GitHub 管理文章

1. 将本仓库推送到 GitHub（公开仓库最省事；私有仓库需在设置里填写 **Token**）。
2. 编辑根目录下的 `content/manifest.json` 维护文章列表，在 `content/posts/` 下新增或修改 `.md` 正文。
3. 在网站页脚打开 **简易设置**：勾选 **从 GitHub 加载**，填写 **用户名、仓库名、分支**（如 `main`）、**manifest 路径**（默认 `content/manifest.json`），保存。

`manifest.json` 中每一项需包含 **`slug`** 与 **`file`**（相对仓库根的路径）。顶层 **`blogDescription`** 用于 Next 的 **关于** 页（可多行）；**`blogName`** 为站名。正文支持可选 **YAML 头信息**（`title`、`date`、`tags`、`slug`、`cover`、`excerpt` 等），与 manifest 字段会合并使用。头像与外链等见 **`content/site.json`**（主要由 Next 侧栏使用）。

### 部署到 GitHub Pages

1. 仓库 **Settings → Pages**，将 **Source** 设为 **GitHub Actions**。
2. 推送到 `main` 或 `master` 分支，由 `.github/workflows/pages.yml` 将仓库根目录部署为静态站点。

若访问地址为 **`https://用户名.github.io/仓库名/`**，页面使用相对路径引用 `css/`、`js/`，与 Hash 路由兼容，无需额外配置伪静态。

### 不用界面预填配置

在 `index.html` 里、引入 `js/app.js` **之前** 可写入 `window.blogConfig`（含 `github` 对象），效果与在「简易设置」里填写一致，便于 Fork 后固定自己的仓库。

### 浏览器

建议使用最新版本的 Chrome、Safari 或 Firefox。

### 许可

仓库未默认附带许可证文件；若需要开源条款，请在 Fork 中自行添加。

---

## Git 代理提示 · Git proxy note

**EN:** If Git reports `Failed to connect to github.com ... via 127.0.0.1`, Git is using a local proxy. Ensure your proxy app is running on the configured port, or run `git config --global --unset http.proxy` and `git config --global --unset https.proxy` to disable it.

**中文：** 若 Git 提示经 `127.0.0.1` 连接 GitHub 失败，说明配置了本机代理。请确认代理软件已开启且端口正确，或使用 `git config --global --unset http.proxy` 与 `https.proxy` 取消代理后再试。
