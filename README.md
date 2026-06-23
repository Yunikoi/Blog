# Minimal Personal Blog · 极简个人博客

个人学习笔记与复习资料站。**Yuni** · [GitHub](https://github.com/Yunikoi/Blog) · [Pages 静态站](https://yunikoi.github.io/Blog)

| 对比 | 根目录静态站 | `web/` Next.js |
|------|-------------|----------------|
| 部署 | GitHub Pages（默认） | Vercel 等，Root Directory = `web` |
| 文章列表 | `manifest.json` 的 `posts[]` | 自动扫描 `content/posts/*.md` |
| 公式 / 测验 | 不支持 | KaTeX、`/quiz` 背单词 |
| 本地运行 | `npx --yes serve .` | `cd web && npm run dev` |

两套界面共用根目录 **`content/`**。编辑请以 **`content/`** 为准；Next 在 dev/build 前会同步到 `web/content/`（勿在 `web/content/` 长期手写）。

---

## 快速开始

**写新文章：** 在 `content/posts/` 新建 `.md`，可加 YAML 头：

```markdown
---
title: 文章标题
date: 2026-06-19
tags: 学习/科目
column: 学习笔记
toc: true
---

正文…
```

**本地预览（推荐 Next，支持公式与测验）：**

```bash
cd web
npm install
npm run dev          # http://localhost:3000
npm run dev:lan      # 0.0.0.0，手机同 Wi‑Fi 可访问
```

**静态站预览：** 在仓库根目录执行 `npx --yes serve .`，浏览器打开提示地址。

**推送后：** `main` 分支 push 即触发 GitHub Pages；Next 版连 Vercel 并设 Root Directory 为 `web`。

---

## Next.js 应用（`web/`）

- **同步：** `scripts/sync-content.mjs` 与 `build-quiz-bank.mjs` 在 `predev` / `prebuild` 自动执行。
- **配置：** `content/manifest.json`（站名、简介）、`site.json`（头像、链接、音乐）、`tags.json`（可选，按 slug 补标签）。
- **阅读：** GFM、KaTeX（`$…$` / `$$…$$`）、宽屏 TOC、标签树、路由淡入淡出、底栏音乐播放器。
- **背单词 `/quiz`：** 文中 `#### 单词：释义` 会编入 `public/quiz-bank.json`；支持看词选义 / 看义选词，进度存浏览器。
- **路由：** `/`、`/posts/[slug]`、`/tags`、`/tags/[tag]`、`/quiz`、`/about`、`/feed.xml`。

生产环境：`npm run build` → `npm run start`。Vercel 连接仓库后 Root Directory 选 `web`（见 `web/vercel.json`）。

### 内容类型（本仓库示例）

高考数学 / 日语语法、JLPT、雅思、Java / 算法 / 软工期末攻略、大模型课程笔记、学习日志等。标签用斜杠分层（如 `学习/数学/高考`）。

---

## 静态站（根目录）

纯 HTML / CSS / JS，Hash 路由（`#/`, `#/post/slug`, `#/about`, `#/tags`），浅色 / 深色主题，阅读进度与目录，页脚 **简易设置** 可开关 GitHub 拉取。

**GitHub 模式：** 在页脚启用 **从 GitHub 加载**，填写用户名、仓库、分支、`content/manifest.json` 路径。`manifest.json` 示例：

```json
{
  "blogName": "站名",
  "blogDescription": "关于页简介",
  "posts": [
    {
      "slug": "my-post",
      "title": "标题",
      "date": "2026-05-12",
      "tags": ["Note"],
      "file": "content/posts/my-post.md"
    }
  ]
}
```

预填配置：在 `index.html` 引入 `js/app.js` 之前设置 `window.blogConfig.github`。

---

## 目录结构

```text
Blog/
├── content/                 # 内容源（Next 构建前同步到 web/content）
│   ├── manifest.json
│   ├── site.json
│   ├── tags.json
│   └── posts/*.md
├── web/                     # Next.js 14（App Router）
│   ├── app/
│   ├── components/
│   ├── public/              # 静态资源、quiz-bank.json、music/
│   └── scripts/             # sync-content.mjs, build-quiz-bank.mjs
├── index.html, css/, js/    # 静态站
└── .github/workflows/pages.yml
```

---

## Git 代理与排错

**TLS / 连不上 GitHub（Clash 等，端口常为 7897）：**

```powershell
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

取消代理：`git config --global --unset http.proxy` 与 `https.proxy`。

**`inflate: data stream error`：** `.git/objects` 对象损坏。删除报错 loose object → `git fetch origin` → `git restore --staged <文件>` → 重新 `git add`（大文件暂存中断时常见）。

---

## English (brief)

Two UIs share **`content/`**: a **vanilla static** site at repo root (default **GitHub Pages**), and a **Next.js 14** app in **`web/`** (KaTeX, vocab quiz, tag tree). Next scans all `content/posts/*.md`; the static site uses `manifest.posts[]`. Run Next with `cd web && npm install && npm run dev`. Deploy Next on Vercel with root directory `web`.
