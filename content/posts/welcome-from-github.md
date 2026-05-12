---
title: 这是一篇来自 GitHub 的文章
date: 2026-05-10
tags: ["GitHub", "博客"]
slug: welcome-from-github
cover: null
---

## 工作原理

把博客静态文件和 **`content/manifest.json`** 放在同一个公开仓库里。`manifest.json` 列出每篇文章的元信息与对应的 **Markdown 文件路径**（相对仓库根目录）。

读者打开站点时，浏览器会请求：

`https://raw.githubusercontent.com/<你的用户名>/<仓库名>/<分支>/content/manifest.json`

进入文章后再拉取对应的 `.md` 正文并渲染。

> 你只需要编辑仓库里的 Markdown，提交推送，无需后端。

### 新建文章步骤

1. 在 `content/posts/` 下新建 `你的文章.md`（可用下方 YAML 头信息）。
2. 在 `content/manifest.json` 的 `posts` 数组里追加一项：`slug`、`title`、`date`、`tags`、`excerpt`、`file`。
3. `git push` 到 GitHub，刷新博客页面即可（可稍等 CDN 缓存）。

```text
可选：在「简易设置」里填写 GitHub 用户名、仓库名并勾选「从 GitHub 加载」。
未启用时仍使用内置演示文章。
```
