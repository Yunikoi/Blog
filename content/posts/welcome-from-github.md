---
title: 这是一篇来自 GitHub 的文章
date: 2026-05-10
slug: welcome-from-github
cover: null
---

## 工作原理

把博客静态文件、**`content/manifest.json`**（站点标题等）与 **`content/tags.json`**（各篇文章的标签）放在同一个公开仓库里。开启自动扫描后，**`content/posts/*.md`** 会全部出现在首页，无需在 manifest 里逐条登记。

读者打开站点时，浏览器会请求：

`https://raw.githubusercontent.com/<你的用户名>/<仓库名>/<分支>/content/manifest.json`

进入文章后再拉取对应的 `.md` 正文并渲染。

> 你只需要编辑仓库里的 Markdown，提交推送，无需后端。

### 新建文章步骤

1. 在 `content/posts/` 下新建 `你的文章.md`（可用 YAML 写标题等，**不要**在 md 里写 `tags`，标签改在 `content/tags.json`）。
2. 在 `content/tags.json` 里为你的 `slug` 配上标签数组。
3. `git push` 到 GitHub；若开启「自动扫描」，无需再改 `manifest.json` 的 `posts` 列表。

```text
可选：在「简易设置」里填写 GitHub 用户名、仓库名并勾选「从 GitHub 加载」。
未启用时仍使用内置演示文章。
```
