# Minimal Personal Blog · 极简个人博客

个人学习笔记与复习资料站。**Yuni** · 仓库：[github.com/Yunikoi/Blog](https://github.com/Yunikoi/Blog) · 静态站：[yunikoi.github.io/Blog](https://yunikoi.github.io/Blog)

This repository contains **two** ways to use the same Markdown-centric content:

1. **Classic static site** at the repo root: **vanilla HTML, CSS, and JavaScript** with a hash router—matches the default **GitHub Pages** workflow (`.github/workflows/pages.yml` publishes the repo root).
2. **Next.js 14 app** in **`web/`** (App Router): home, posts with optional TOC, tag tree, About page, optional footer music, and synced content from the root **`content/`** folder.

**中文：** 仓库里有两套界面共用 **`content/`** 里的文章与配置：根目录 **纯静态** 博客（适合当前 Pages 工作流），以及 **`web/`** 下的 **Next.js** 阅读站（三栏布局、标签树、LaTeX 公式、背单词测验、可选底栏音乐等）。编辑内容请以仓库根目录 **`content/`** 为准；Next 在 `npm run dev` / `npm run build` 时会把其复制到 `web/content/`（勿在 `web/content/` 长期手写）。

---

## Next.js app (`web/`)

### Features

- **Content sync:** `web/scripts/sync-content.mjs` copies `../content` → `web/content` before dev/build (`predev` / `prebuild` in `web/package.json`).
- **Post discovery:** Next **scans** `content/posts/*.md` (YAML front matter: `title`, `date`, `updated`, `tags`, `column`, `toc`, `excerpt`, …). Optional `content/tags.json` merges extra tags per slug. `manifest.json` supplies **`blogName`** / **`blogDescription`** only (About + metadata); the static site’s `manifest.posts[]` list is **not** used by Next.
- **Config files (root `content/`):** `manifest.json`, `site.json` (profile, links, optional `music` playlist), `tags.json` (optional), Markdown in `posts/`.
- **Reading UX:** GFM Markdown, **KaTeX** math (`$…$`, `$$…$$`), sticky TOC on wide screens, lyric line in TOC panel when applicable, soft **blur / fade** route transitions (`prefers-reduced-motion` disables), semi-transparent bottom music player.
- **Vocab quiz (`/quiz`):** `web/scripts/build-quiz-bank.mjs` (also in `predev` / `prebuild`) builds `public/quiz-bank.json` from lines like `#### 单词：释义` in any post—works on static deploy without a live API. Modes: term→definition or definition→term; progress stored in browser.
- **Routes:** `/`, `/posts/[slug]`, `/tags`, `/tags/[tag]`, `/quiz`, `/about`, `/feed.xml`.

### Run locally

```bash
cd web
npm install
npm run dev          # http://localhost:3000
npm run dev:lan      # bind 0.0.0.0 for phone on same Wi‑Fi
```

Production: `npm run build` then `npm run start`.

### Quiz card format (in any `content/posts/*.md`)

```markdown
#### 単語：意思
#### apple：苹果
```

Only `####` headings with a Chinese colon `：` or ASCII `:` between term and definition are picked up.

### Deploy note

GitHub Actions in this repo deploys the **static root** to Pages. Host **`web/`** on a Node-compatible platform (e.g. Vercel, root directory `web`) if you want the Next app—including `/quiz` and LaTeX—in production.

**Vercel (Next app):** connect the repo, set **Root Directory** to `web`, framework auto-detected via `web/vercel.json`. `prebuild` runs content sync and quiz-bank generation.

### Content in `content/posts/`

Markdown notes with YAML front matter (`title`, `date`, `tags`, `column`, `toc`, …). Examples in this repo: gaokao math/Japanese grammar, JLPT, IELTS, Java / algorithms / software-architecture exam guides, LLM course notes, study logs. Tag tree uses slash paths (e.g. `学习/数学/高考`).

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
├── content/                 # Shared source of truth (synced to web/content before Next dev/build)
│   ├── manifest.json        # blogName, blogDescription; posts[] for static GitHub mode
│   ├── site.json            # Profile, links, optional music (Next sidebar + player)
│   ├── tags.json            # Optional per-slug tag overrides (Next)
│   └── posts/*.md           # Articles + optional #### term：def lines for /quiz
├── web/                     # Next.js 14 app (App Router)
│   ├── app/                 # pages, /quiz, /feed.xml, music & quiz API routes
│   ├── components/          # VocabQuiz, MusicPlayer, TagTree, …
│   ├── lib/
│   ├── public/              # Assets, generated quiz-bank.json, music/*.mp3
│   ├── scripts/
│   │   ├── sync-content.mjs
│   │   └── build-quiz-bank.mjs
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

Next.js 版功能（含 **背单词 /quiz**、**KaTeX 公式**、标签树、音乐播放器）、本地运行与部署说明见上文 **「Next.js app (`web/`)」** 一节；以下为根目录 **静态版** 说明。

**与 Next 的差异：** 静态站通过 **简易设置** 或 `manifest.json` 的 **`posts[]`** 维护文章列表；Next 直接读取 **`content/posts/`** 下全部 `.md`，`manifest` 只提供站名与简介。

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

Next.js 阅读站在 **`web/`** 目录：`cd web`，执行 `npm install` 与 `npm run dev`（局域网访问用 `npm run dev:lan`；详见文件开头的 **Next.js app** 一节）。

### 背单词（`/quiz`）

在任意 `content/posts/*.md` 里用四级标题写词条，构建时会生成 `public/quiz-bank.json`：

```markdown
#### 単語：意思
```

支持 **看词选义** / **看义选词**；部署到 Vercel 等后手机访问 `你的域名/quiz` 即可，无需本机 API。

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

**EN:** If `git push` / `git fetch` fails with `TLS connect error: unexpected eof` or `Failed to connect to github.com ... via 127.0.0.1`, Git is using a local proxy (common with Clash on port **7897**).

1. Ensure the proxy app is running and the port matches your Git config.
2. For Clash-style mixed ports, **HTTP proxy** often works better than SOCKS5:

   ```powershell
   git config --global http.proxy http://127.0.0.1:7897
   git config --global https.proxy http://127.0.0.1:7897
   ```

3. To disable proxy entirely: `git config --global --unset http.proxy` and `git config --global --unset https.proxy`.

**中文：** 若 `git push` / `git fetch` 出现 TLS 握手失败或经 `127.0.0.1` 连不上 GitHub，多半是本机代理（如 Clash **7897**）与 Git 不匹配。先确认代理已开、端口一致；Clash 混合端口下可试 **HTTP 代理**（见上命令）。不需要代理时用 `--unset` 取消 `http.proxy` / `https.proxy`。

**对象损坏（`inflate: data stream error`）：** 本地 `.git/objects` 中某个对象损坏时，`git status` 会失败。可删除报错路径下的 loose object，执行 `git fetch origin`，再对涉及文件 `git restore --staged` 后重新 `git add`（大文件暂存中断时较常见）。
