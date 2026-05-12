# Minimal Personal Blog · 极简个人博客

**English:** A calm, reading-focused personal blog built with **vanilla HTML, CSS, and JavaScript**—no frameworks. Optional **GitHub-backed** content (manifest + Markdown) and **GitHub Pages** deployment.

**中文：** 面向阅读的极简个人博客，**纯 HTML / CSS / JavaScript**，无前端框架。支持可选的 **GitHub 文章源**（清单 + Markdown）以及 **GitHub Pages** 部署。

---

## English

### Features

- **UI:** Generous whitespace, system / Inter typography, accent color, card list with subtle hover, light / dark theme (auto or manual), smooth theme transitions, `localStorage` for preferences.
- **Routing:** Hash-based SPA (`#/`, `#/post/slug`, `#/about`, `#/tags`, `#/tags/tag`) without full page reloads; ~200 ms view transitions.
- **Article view:** Markdown subset (headings, paragraphs, blockquotes, fenced code with copy, images, links, inline code), reading progress bar, back-to-top, desktop TOC + mobile collapsible TOC, prev/next navigation.
- **GitHub mode:** Load `manifest.json` from `raw.githubusercontent.com`, then fetch each post body from the repo. Falls back to built-in demo posts if the request fails.
- **Settings (footer):** Site title, tagline, theme, GitHub source toggles, optional PAT for private repos (stored in browser only).

### Project layout

```text
Blog/
├── index.html          # Shell + settings panel
├── css/styles.css      # Layout, theme tokens, components
├── js/app.js           # Router, markdown, GitHub fetch, theme
├── content/
│   ├── manifest.json   # Post index (when using GitHub)
│   └── posts/*.md      # Markdown bodies
└── .github/workflows/
    └── pages.yml       # GitHub Actions → Pages
```

### Run locally

Open `index.html` in a browser, or serve the folder (recommended):

```bash
npx --yes serve .
```

### Use GitHub as the content source

1. Push this repository (or your fork) to GitHub **as a public repo** (or use a PAT for private repos).
2. Edit `content/manifest.json` (post metadata + `file` paths) and add Markdown under `content/posts/`.
3. On the site, open **简易设置** at the bottom: enable **从 GitHub 加载**, enter **username**, **repository**, **branch** (e.g. `main`), and **manifest path** (default `content/manifest.json`), then save.

`manifest.json` shape:

```json
{
  "blogName": "Your site name",
  "blogDescription": "One-line description",
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

### 功能概览

- **界面：** 留白、系统字体与 Inter、单一强调色、卡片列表与悬停微动效、浅色 / 深色 / 跟随系统、主题色过渡、`localStorage` 保存偏好。
- **路由：** Hash 单页（`#/`, `#/post/文章slug`, `#/about`, `#/tags`, `#/tags/标签`），无整页刷新，视图切换约 200 ms 淡入淡出。
- **文章页：** 子集 Markdown（标题、段落、引用、代码块与复制、图片、链接、行内代码）、顶部阅读进度、返回顶部、桌面端目录 + 移动端折叠目录、上一篇 / 下一篇。
- **GitHub 模式：** 从 `raw.githubusercontent.com` 拉取 `manifest.json`，再按需拉取各篇 `.md` 正文；拉取失败时自动回退到内置演示文章。
- **简易设置（页脚）：** 站名、一句话介绍、主题、GitHub 源开关与仓库信息；可选 Token（仅保存在本机浏览器，适合私有仓库）。

### 目录结构

见上文 **Project layout** 一节（与英文一致）。

### 本地运行

直接用浏览器打开 `index.html`，或使用本地静态服务（推荐）：

```bash
npx --yes serve .
```

### 使用 GitHub 管理文章

1. 将本仓库推送到 GitHub（公开仓库最省事；私有仓库需在设置里填写 **Token**）。
2. 编辑根目录下的 `content/manifest.json` 维护文章列表，在 `content/posts/` 下新增或修改 `.md` 正文。
3. 在网站页脚打开 **简易设置**：勾选 **从 GitHub 加载**，填写 **用户名、仓库名、分支**（如 `main`）、**manifest 路径**（默认 `content/manifest.json`），保存。

`manifest.json` 中每一项需包含 **`slug`** 与 **`file`**（相对仓库根的路径）。正文支持可选 **YAML 头信息**（`title`、`date`、`tags`、`slug`、`cover`、`excerpt` 等），与 manifest 字段会合并使用。

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
