/**
 * Minimal blog — vanilla SPA
 * Data: window.blogConfig, window.blogData
 */
(function () {
  "use strict";

  const STORAGE_KEY = "minimal_blog_prefs_v1";
  const DEFAULT_CONFIG = {
    blogName: "纸间",
    blogDescription: "写一点技术、设计与生活的留白。",
    heroHighlight: "最新文章 · 编者按",
    themeMode: "auto",
    github: {
      enabled: false,
      user: "",
      repo: "",
      branch: "main",
      manifestPath: "content/manifest.json",
    },
  };

  window.blogConfig = window.blogConfig || { ...DEFAULT_CONFIG };
  window.blogConfig.github = Object.assign(
    {},
    DEFAULT_CONFIG.github,
    window.blogConfig.github && typeof window.blogConfig.github === "object"
      ? window.blogConfig.github
      : {}
  );

  const unsplash = (id, w, h) =>
    `https://images.unsplash.com/photo-${id}?auto=format&fit=crop&w=${w}&h=${h}&q=80`;

  window.blogData = window.blogData || [
    {
      slug: "quiet-ui",
      title: "安静界面里的克制与信任",
      date: "2026-04-18",
      tags: ["设计", "UX"],
      cover: unsplash("1558655146-d09347e92766", 800, 500),
      excerpt:
        "当界面不再争抢注意力，读者反而更愿意停留。克制不是贫乏，而是把密度留给真正重要的句子与节奏。",
      body: `## 为什么“少”更难

设计极简界面时，最常见的误区是把**留白**当成空白。事实上，留白是节奏：它让眼睛知道下一口该读哪里。

> 好的排版像呼吸：吸气是标题，呼气是段落之间的停顿。

### 三个可操作的练习

1. 把主色限制在两种：文本与强调。
2. 先写内容结构，再补装饰。
3. 用同一套间距刻度（例如 4/8/16/32）。

\`\`\`css
:root {
  --line: 1.7;
  --measure: 65ch;
}
article { max-width: var(--measure); line-height: var(--line); }
\`\`\`

![排版与纸张](https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1200&q=80)

## 从 Medium 学到的不是样式，而是耐心

顶级阅读产品都在做同一件事：**降低认知噪音**。按钮更少、层级更浅、动画更短。读者会回报你的是“信任感”——他们相信你不会突然弹窗打断。

下一篇我们会聊暗色模式如何影响对比与情绪。`,
    },
    {
      slug: "dark-mode-reading",
      title: "暗色模式：对比、情绪与可读性",
      date: "2026-04-02",
      tags: ["设计", "前端"],
      cover: null,
      excerpt:
        "深色背景不是把白色文字反过来那么简单。对比过高会刺眼，过低会发灰。这里有一套更温和的取舍。",
      body: `## 先把背景从纯黑移开

\`#000000\` 在 OLED 上很酷，但对长文阅读并不友好。试试接近 **#0a0a0a** 或带一点蓝灰的底色，正文用 **#e5e5e5** 而不是纯白。

> 阅读是马拉松，配色是跑鞋：要稳，不要炫。

### 代码块与引用在深色下的层次

给代码区域单独的“凹陷层”，比正文再低一点亮度，读者会自然把视线落在段落上。

\`\`\`javascript
function prefersDark() {
  return window.matchMedia("(prefers-color-scheme: dark)").matches;
}
\`\`\`

## 平滑过渡主题

切换主题时，给 \`body\` 一个短暂的 \`transition\`，背景与文字同时变化，避免“闪烁跳变”。

![夜景城市](https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=1200&q=80)

当你把暗色当成一种“氛围”而不是皮肤，界面会安静很多。`,
    },
    {
      slug: "writing-ship",
      title: "写作系统：从草稿到发布的最短路径",
      date: "2026-03-21",
      tags: ["写作", "效率"],
      cover: unsplash("1455390582262-044c14ba2f5c", 800, 500),
      excerpt:
        "灵感很碎，发布要稳。用最小可行流程把想法落成文章：提纲、例证、删词、朗读一遍。",
      body: `## 我用的四张卡片

**捕捉**：一句话记录观点，不追求完美。  
**结构**：只写二级标题，像目录一样铺开。  
**例证**：每个观点至少一个故事、数据或比喻。  
**删减**：删掉 20% 仍然成立的句子。

> 发布不是结束，是下一次对话的开始。

### Markdown 作为中间格式

Markdown 让你专注语义，而不是样式。下面是一段列表式 checklist：

- 标题是否回答了读者真正的问题？
- 第一段是否在 120 字内给出承诺？
- 结尾是否留下一个可执行的小动作？

\`\`\`markdown
> 读者的时间很贵，别让他们猜你要说什么。
\`\`\`

![笔记本与咖啡](https://images.unsplash.com/photo-1517842645767-c639b8806036?auto=format&fit=crop&w=1200&q=80)

把“写完”定义成“可以被陌生人读懂”，你会少很多自我感动。`,
    },
    {
      slug: "perf-native",
      title: "原生三件套也能做出顺滑体验",
      date: "2026-02-28",
      tags: ["前端", "性能"],
      cover: unsplash("1461749280684-dccba630e2f6", 800, 500),
      excerpt:
        "没有框架并不意味着粗糙。路由、过渡、缓存偏好——用少量代码组织好状态，页面会轻得像一张纸。",
      body: `## 体验来自细节堆叠

**200ms 的淡入**足够让眼睛完成一次“场景切换”，再长就显得拖沓。阅读进度条保持 **2px** 高度，它应该是提示，而不是主角。

> 性能不是数字，是“是否被打断”的主观感受。

### 监听滚动时的节流

\`\`\`javascript
function onScrollThrottled(fn, ms) {
  let t = 0;
  return () => {
    const n = Date.now();
    if (n - t > ms) { t = n; fn(); }
  };
}
\`\`\`

## 本地存储要谨慎

只存**偏好**（主题、站点标题），不要把大段内容塞进 \`localStorage\`。读者刷新页面时，世界仍应是原来的样子。

![代码屏幕](https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80)

当你愿意为基础体验多花半小时，用户会回报你“像原生应用一样可靠”的印象。`,
    },
    {
      slug: "life-signals",
      title: "生活里的弱信号：如何不被算法牵着走",
      date: "2026-02-06",
      tags: ["生活", "思考"],
      cover: null,
      excerpt:
        "注意力是最稀缺的货币。学会识别那些“微弱但持续”的快乐来源：散步、做饭、和真实的人说话。",
      body: `## 强刺激让人上瘾，弱信号才养人

算法喜欢把情绪推到峰值，因为峰值最容易被点击。但峰值也会迅速回落，留下空洞。

> 你不需要更刺激，你需要更连贯。

### 三个弱信号例子

1. 早晨同样路线但不同天空。
2. 一本书读得很慢，却常常想起。
3. 朋友发来的长语音里背景噪音。

\`\`\`text
强刺激：短视频、热搜、争吵
弱信号：散步、手写、慢读
\`\`\`

## 给博客留一点“慢”

个人博客可以反潮流：**不追热点、不制造焦虑**。把更新频率调低，把每篇写厚一点，读者会记得你。

![森林小径](https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1200&q=80)

当你开始珍惜弱信号，生活会悄悄变宽。`,
    },
    {
      slug: "typography-notes",
      title: "字体与行高：把正文交给系统栈",
      date: "2026-01-15",
      tags: ["设计", "排版"],
      cover: unsplash("1561070791-2526d30994b5", 800, 500),
      excerpt:
        "Inter 与系统 UI 字体混用并不冲突。关键是字号梯度、行高 1.6–1.8、以及段落间距略大于行距。",
      body: `## 系统字体为什么仍然顶级

在 macOS 与 iOS 上，\`-apple-system\` 与 \`SF Pro Text\` 经过大量场景调校。它们在小字号下的可读性，往往胜过许多“好看但难读”的展示字体。

> 排版的第一目标是“读完”，第二目标才是“好看”。

### 行高与行长

当行长在 **60–75 字符** 之间，\`line-height: 1.7\` 通常最舒服。移动端略小字号、略窄边距，桌面端略大字号。

\`\`\`css
body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
  line-height: 1.7;
}
\`\`\`

## 渐进式字号

用 \`clamp()\` 在 15–18px 之间平滑过渡，比断点硬切更自然。读者不会察觉“跳了一格”，但会感觉到“哪里更顺”。

![字体排印](https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&w=1200&q=80)

把字体当成界面的一部分去调，而不是最后贴上的皮肤。`,
    },
    {
      slug: "newsletter-era",
      title: "通讯写作时代，博客还剩什么？",
      date: "2025-12-08",
      tags: ["写作", "设计"],
      cover: unsplash("1557804507-8ccb7b73b38e", 800, 500),
      excerpt:
        "Substack 把作者和读者拉得很近，但博客仍可以是“自己的花园”：域名、版式、节奏，完全属于你。",
      body: `## 花园与广场

通讯像广场：热闹、更新快、评论即反馈。博客像花园：你可以慢慢种一棵树，等它长大。

> 广场需要掌声，花园只需要阳光。

### 博客的独特价值

- **版式**：你可以为长文服务，而不是为订阅按钮服务。
- **归档**：时间轴是叙事，而不是算法推荐。
- **所有权**：HTML 文件在你手里。

\`\`\`html
<article>
  <h1>标题属于我</h1>
  <p>段落也属于我。</p>
</article>
\`\`\`

## 把两者结合起来

很多作者把通讯当入口，把博客当深度存档。读者在不同深度停留，你也在不同深度表达。

![信件与键盘](https://images.unsplash.com/photo-1525182008055-f88b95ff7980?auto=format&fit=crop&w=1200&q=80)

无论你选哪条路，真诚都比技巧更稀有。`,
    },
  ];

  function deepClonePosts(arr) {
    return arr.map((p) => ({
      ...p,
      tags: Array.isArray(p.tags) ? [...p.tags] : [],
    }));
  }

  const embeddedBlogData = deepClonePosts(window.blogData);

  let blogDataLoadState = { ok: true, error: null, source: "embedded" };
  const BODY_CACHE_PREFIX = "minimal_blog_body_v1:";

  /* ---------- utilities ---------- */
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function parseDate(iso) {
    if (!iso || !String(iso).trim()) return "日期待定";
    const d = new Date(iso + "T12:00:00");
    return d.toLocaleDateString("zh-CN", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  }

  function readingMinutesFromMarkdown(md) {
    const words = md.replace(/```[\s\S]*?```/g, "").length;
    return Math.max(1, Math.round(words / 650));
  }

  function loadPrefs() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return {};
      return JSON.parse(raw);
    } catch {
      return {};
    }
  }

  function savePrefs(prefs) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs));
    } catch {
      /* ignore */
    }
  }

  function readingMinutesForPost(p) {
    if (p.body && String(p.body).trim()) return readingMinutesFromMarkdown(p.body);
    const t = (p.excerpt || "").length + (p.title || "").length * 2;
    return Math.max(1, Math.min(45, Math.round(t / 420)));
  }

  function rawContentUrl(filePath) {
    const gh = window.blogConfig.github;
    const u = String(gh.user || "").trim();
    const r = String(gh.repo || "").trim();
    const b = String(gh.branch || "main").trim();
    const segs = String(filePath || "")
      .replace(/^\/+/, "")
      .split("/")
      .filter(Boolean)
      .map((s) => encodeURIComponent(s))
      .join("/");
    return `https://raw.githubusercontent.com/${encodeURIComponent(u)}/${encodeURIComponent(
      r
    )}/${encodeURIComponent(b)}/${segs}`;
  }

  function githubFetch(url) {
    const token = String((loadPrefs().githubToken || "")).trim();
    const headers = {};
    if (token) headers.Authorization = `Bearer ${token}`;
    return fetch(url, { headers, cache: "no-store" });
  }

  function parseFrontmatter(text) {
    const t = text.replace(/^\uFEFF/, "");
    if (!t.startsWith("---")) return { meta: {}, body: t };
    const nl = t.indexOf("\n");
    if (nl === -1) return { meta: {}, body: t };
    const end = t.indexOf("\n---", 3);
    if (end === -1) return { meta: {}, body: t };
    const fmRaw = t.slice(nl + 1, end).trim();
    const body = t.slice(end + 4).replace(/^\r?\n/, "");
    const meta = {};
    fmRaw.split(/\n/).forEach((line) => {
      const m = line.match(/^([\w-]+):\s*(.*)$/);
      if (!m) return;
      const key = m[1].trim();
      let val = m[2].trim();
      if (key === "tags") {
        if (val.startsWith("[")) {
          try {
            meta.tags = JSON.parse(val);
          } catch {
            meta.tags = val.split(/,\s*/).filter(Boolean);
          }
        } else {
          meta.tags = val.split(/,\s*/).filter(Boolean);
        }
        return;
      }
      if (key === "cover" && (val === "null" || val === "")) {
        meta.cover = null;
        return;
      }
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      meta[key] = val;
    });
    return { meta, body };
  }

  function applyMarkdownToPost(post, rawMarkdown) {
    const { meta, body } = parseFrontmatter(rawMarkdown);
    if (meta.title) post.title = meta.title;
    if (meta.date) post.date = meta.date;
    if (meta.slug) post.slug = meta.slug;
    if (meta.cover !== undefined) post.cover = meta.cover === null ? null : meta.cover;
    if (Array.isArray(meta.tags)) post.tags = meta.tags;
    if (meta.excerpt) post.excerpt = meta.excerpt;
    post.body = body;
  }

  function loadBodyCache(slug) {
    try {
      return sessionStorage.getItem(BODY_CACHE_PREFIX + slug);
    } catch {
      return null;
    }
  }

  function saveBodyCache(slug, text) {
    try {
      sessionStorage.setItem(BODY_CACHE_PREFIX + slug, text);
    } catch {
      /* ignore */
    }
  }

  async function loadBlogDataSource() {
    const gh = window.blogConfig.github;
    blogDataLoadState = { ok: true, error: null, source: "embedded" };

    if (!gh || !gh.enabled || !String(gh.user || "").trim() || !String(gh.repo || "").trim()) {
      window.blogData = deepClonePosts(embeddedBlogData);
      return;
    }

    const path = String(gh.manifestPath || "content/manifest.json").trim();
    const url = rawContentUrl(path);

    try {
      const res = await githubFetch(url);
      if (!res.ok) throw new Error(`无法拉取 manifest（HTTP ${res.status}）`);
      const manifest = await res.json();
      if (typeof manifest.blogName === "string" && manifest.blogName.trim()) {
        window.blogConfig.blogName = manifest.blogName.trim();
      }
      if (typeof manifest.blogDescription === "string") {
        window.blogConfig.blogDescription = manifest.blogDescription;
      }
      if (typeof manifest.heroHighlight === "string" && manifest.heroHighlight.trim()) {
        window.blogConfig.heroHighlight = manifest.heroHighlight.trim();
      }

      const list = Array.isArray(manifest.posts) ? manifest.posts : [];
      window.blogData = list
        .filter((item) => String(item.file || "").trim() && String(item.slug || "").trim())
        .map((item) => {
        const tags = Array.isArray(item.tags)
          ? item.tags
          : typeof item.tags === "string"
            ? item.tags.split(/,\s*/).filter(Boolean)
            : [];
        return {
          slug: String(item.slug || "").trim() || "untitled",
          title: (item.title != null && String(item.title)) || String(item.slug || "未命名"),
          date: String(item.date || "").trim(),
          tags,
          cover: item.cover != null ? item.cover : null,
          excerpt: String(item.excerpt || "").trim(),
          body: "",
          _githubFile: String(item.file || "").trim(),
        };
      });
      blogDataLoadState = { ok: true, error: null, source: "github" };
    } catch (e) {
      console.error(e);
      window.blogData = deepClonePosts(embeddedBlogData);
      blogDataLoadState = {
        ok: false,
        error: e && e.message ? e.message : String(e),
        source: "embedded-fallback",
      };
    }
  }

  function sortedPosts() {
    return [...window.blogData].sort((a, b) => (a.date < b.date ? 1 : -1));
  }

  function getPost(slug) {
    return window.blogData.find((p) => p.slug === slug);
  }

  function allTags() {
    const set = new Set();
    window.blogData.forEach((p) => (p.tags || []).forEach((t) => set.add(t)));
    return [...set].sort((a, b) => a.localeCompare(b, "zh-CN"));
  }

  /* ---------- markdown (subset) ---------- */
  function inlineFormat(text) {
    let s = escapeHtml(text);
    s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
    s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    s = s.replace(/\*([^*]+)\*/g, "<em>$1</em>");
    s = s.replace(
      /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
    );
    s = s.replace(
      /!\[([^\]]*)\]\((https?:\/\/[^\s)]+)\)/g,
      '<img src="$2" alt="$1" loading="lazy" />'
    );
    return s;
  }

  function parseMarkdown(md) {
    const toc = [];
    let tocIdx = 0;

    const lines = md.replace(/\r\n/g, "\n").split("\n");
    const blocks = [];
    let i = 0;

    while (i < lines.length) {
      const line = lines[i];

      if (line.startsWith("```")) {
        const lang = line.slice(3).trim();
        const codeLines = [];
        i++;
        while (i < lines.length && !lines[i].startsWith("```")) {
          codeLines.push(lines[i]);
          i++;
        }
        if (i < lines.length && lines[i].startsWith("```")) i++;
        blocks.push({ type: "code", lang, code: codeLines.join("\n") });
        continue;
      }

      if (line.startsWith(">")) {
        const quote = [];
        while (i < lines.length && lines[i].startsWith(">")) {
          quote.push(lines[i].replace(/^>\s?/, ""));
          i++;
        }
        blocks.push({ type: "quote", text: quote.join("\n") });
        continue;
      }

      if (/^#{1,6}\s+/.test(line)) {
        const m = line.match(/^(#{1,6})\s+(.*)$/);
        const level = m[1].length;
        const raw = m[2].trim();
        const id = "section-" + ++tocIdx;
        if (level === 2 || level === 3) {
          toc.push({ id, text: raw.replace(/\*\*|\*/g, ""), level });
        }
        blocks.push({ type: "heading", level, text: raw, id });
        i++;
        continue;
      }

      if (line.trim() === "") {
        i++;
        continue;
      }

      const para = [];
      while (
        i < lines.length &&
        lines[i].trim() !== "" &&
        !lines[i].startsWith("```") &&
        !lines[i].startsWith(">") &&
        !/^#{1,6}\s+/.test(lines[i])
      ) {
        para.push(lines[i]);
        i++;
      }
      blocks.push({ type: "p", text: para.join("\n") });
    }

    let html = "";
    for (const b of blocks) {
      if (b.type === "code") {
        const escaped = escapeHtml(b.code);
        html += `<div class="code-block-wrap"><pre><code class="language-${escapeHtml(
          b.lang || "text"
        )}">${escaped}</code></pre><button type="button" class="code-copy" data-copy>${escapeHtml(
          "复制"
        )}</button></div>`;
      } else if (b.type === "quote") {
        html += `<blockquote><p>${inlineFormat(b.text)}</p></blockquote>`;
      } else if (b.type === "heading") {
        const tag = "h" + Math.min(6, Math.max(1, b.level));
        html += `<${tag} id="${escapeHtml(b.id)}">${inlineFormat(b.text)}</${tag}>`;
      } else if (b.type === "p") {
        const parts = b.text.split(/\n{2,}/);
        for (const part of parts) {
          if (part.trim()) html += `<p>${inlineFormat(part.trim())}</p>`;
        }
      }
    }

    return { html, toc };
  }

  function enhanceCodeCopy(root) {
    root.querySelectorAll(".code-block-wrap").forEach((wrap) => {
      const btn = wrap.querySelector(".code-copy");
      const code = wrap.querySelector("code");
      if (!btn || !code || btn.dataset.bound) return;
      btn.dataset.bound = "1";
      btn.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(code.textContent || "");
          const prev = btn.textContent;
          btn.textContent = "已复制";
          setTimeout(() => {
            btn.textContent = prev;
          }, 1600);
        } catch {
          btn.textContent = "失败";
        }
      });
    });
  }

  function buildTocHtml(toc, variant) {
    if (!toc.length) return "";
    if (variant === "sidebar") {
      return (
        `<nav class="toc-panel" aria-label="文章目录"><p class="toc-panel__title">目录</p>` +
        toc
          .map(
            (t) =>
              `<a href="#${escapeHtml(t.id)}" data-toc-id="${escapeHtml(
                t.id
              )}" style="padding-left:${(t.level - 2) * 0.55 + 0.5}rem">${escapeHtml(
                t.text
              )}</a>`
          )
          .join("") +
        `</nav>`
      );
    }
    const items = toc
      .map(
        (t) =>
          `<li style="margin-left:${(t.level - 2) * 0.75}rem"><a href="#${escapeHtml(
            t.id
          )}">${escapeHtml(t.text)}</a></li>`
      )
      .join("");
    return `<details class="toc-mobile"><summary>目录</summary><ul class="toc-mobile__list">${items}</ul></details>`;
  }

  /* ---------- DOM / router ---------- */
  const viewRoot = document.getElementById("view-root");
  const mainEl = document.getElementById("main");
  const siteLogo = document.getElementById("site-logo");
  const footerBlogName = document.getElementById("footer-blog-name");
  const readingBar = document.getElementById("reading-progress");
  const backToTop = document.getElementById("back-to-top");
  const themeToggle = document.getElementById("theme-toggle");
  const burger = document.getElementById("nav-burger");
  const drawer = document.getElementById("mobile-drawer");
  const settingsPanel = document.getElementById("settings-panel");
  const settingsToggle = document.getElementById("footer-settings-toggle");
  const inputName = document.getElementById("setting-blog-name");
  const inputDesc = document.getElementById("setting-blog-desc");
  const selectTheme = document.getElementById("setting-theme-mode");
  const btnSave = document.getElementById("settings-save");
  const btnReset = document.getElementById("settings-reset");
  const chkGithub = document.getElementById("setting-github-enabled");
  const inputGithubUser = document.getElementById("setting-github-user");
  const inputGithubRepo = document.getElementById("setting-github-repo");
  const inputGithubBranch = document.getElementById("setting-github-branch");
  const inputGithubManifest = document.getElementById("setting-github-manifest");
  const inputGithubToken = document.getElementById("setting-github-token");

  let routeFadeTimer = null;
  let scrollHandler = null;
  let tocObserver = null;
  let firstViewRender = true;

  function applyConfigToDom() {
    const c = window.blogConfig;
    document.title = c.blogName;
    siteLogo.textContent = c.blogName;
    footerBlogName.textContent = c.blogName;
  }

  function parseHash() {
    const raw = (location.hash || "#/").replace(/^#/, "");
    const parts = raw.split("/").filter(Boolean);
    if (parts.length === 0) return { name: "home" };
    if (parts[0] === "post" && parts[1]) return { name: "post", slug: decodeURIComponent(parts[1]) };
    if (parts[0] === "about") return { name: "about" };
    if (parts[0] === "tags") {
      if (parts[1]) return { name: "tags", tag: decodeURIComponent(parts[1]) };
      return { name: "tags" };
    }
    return { name: "home" };
  }

  function navigate(path) {
    location.hash = path.startsWith("#") ? path : "#" + path;
  }

  function setNavActive(route) {
    document.querySelectorAll(".site-nav__link").forEach((a) => {
      const nav = a.getAttribute("data-nav");
      const active =
        (route.name === "home" && nav === "home") ||
        (route.name === "tags" && nav === "tags") ||
        (route.name === "about" && nav === "about");
      a.classList.toggle("is-active", !!active);
    });
  }

  function fadeSwap(renderFn) {
    clearTimeout(routeFadeTimer);
    viewRoot.classList.add("is-fading");
    routeFadeTimer = setTimeout(() => {
      Promise.resolve(renderFn())
        .catch((err) => {
          console.error(err);
          viewRoot.innerHTML = `<div class="empty-state"><p>加载失败。</p><p><a href="#/">返回首页</a></p></div>`;
        })
        .finally(() => {
          requestAnimationFrame(() => {
            viewRoot.classList.remove("is-fading");
          });
        });
    }, 200);
  }

  function renderHome(filterTag) {
    const posts = sortedPosts().filter((p) =>
      filterTag ? (p.tags || []).includes(filterTag) : true
    );
    const c = window.blogConfig;
    const latest = posts[0];
    const highlight = latest
      ? `${c.heroHighlight || "最新"} · 《${latest.title}》`
      : c.heroHighlight || "";

    const listHtml = posts
      .map((p) => {
        const ex = p.excerpt || "";
        const mins = readingMinutesForPost(p);
        const thumb = p.cover
          ? `<div class="post-card__thumb"><img src="${escapeHtml(
              p.cover
            )}" alt="" /></div>`
          : `<div class="post-card__thumb post-card__thumb--gradient" style="background-image:linear-gradient(135deg,#0f172a 0%,#1e293b 45%,var(--accent) 100%)"></div>`;
        const tags = (p.tags || [])
          .map((t) => `<span class="tag-pill">${escapeHtml(t)}</span>`)
          .join("");
        return `<a href="#/post/${encodeURIComponent(p.slug)}" class="post-card">
          ${thumb}
          <div class="post-card__body">
            <div class="post-card__meta"><time datetime="${escapeHtml(
              p.date
            )}">${escapeHtml(parseDate(p.date))}</time><span>${mins} 分钟阅读</span></div>
            <h2 class="post-card__title">${escapeHtml(p.title)}</h2>
            <p class="post-card__excerpt">${escapeHtml(ex)}</p>
            <div class="post-card__tags">${tags}</div>
          </div>
        </a>`;
      })
      .join("");

    const filterLine = filterTag
      ? `<p class="filter-bar">正在筛选标签 <strong>${escapeHtml(
          filterTag
        )}</strong> · <a href="#/">查看全部</a></p>`
      : "";

    const ghBanner =
      blogDataLoadState.source === "github"
        ? `<p class="github-source-banner" role="status">当前文章列表来自 GitHub 仓库 <strong>${escapeHtml(
            String(window.blogConfig.github.user || "").trim()
          )}</strong>/<strong>${escapeHtml(
            String(window.blogConfig.github.repo || "").trim()
          )}</strong></p>`
        : "";
    const fallbackBanner =
      !blogDataLoadState.ok && blogDataLoadState.source === "embedded-fallback"
        ? `<p class="github-fallback-banner" role="alert">无法从 GitHub 读取清单（${escapeHtml(
            blogDataLoadState.error || "未知错误"
          )}），已暂时使用内置演示文章。请检查仓库是否公开、路径与分支是否正确。</p>`
        : "";

    viewRoot.innerHTML = `
      <section class="hero">
        <h1 class="hero__title">${escapeHtml(c.blogName)}</h1>
        <p class="hero__desc">${escapeHtml(c.blogDescription)}</p>
        ${
          highlight
            ? `<p class="hero__highlight" role="status">${escapeHtml(highlight)}</p>`
            : ""
        }
      </section>
      ${ghBanner}
      ${fallbackBanner}
      ${filterLine}
      <h2 class="section-label">文章</h2>
      <div class="post-list">${listHtml || `<p class="empty-state">暂无文章。</p>`}</div>
    `;
    readingBar.style.width = "0%";
    readingBar.classList.remove("is-active");
    detachScrollListeners();
  }

  async function renderPostAsync(slug) {
    const post = getPost(slug);
    if (!post) {
      viewRoot.innerHTML = `<div class="empty-state"><p>找不到这篇文章。</p><p><a href="#/">返回首页</a></p></div>`;
      detachScrollListeners();
      return;
    }

    if (post._githubFile && !String(post.body || "").trim()) {
      const cached = loadBodyCache(slug);
      if (cached) {
        applyMarkdownToPost(post, cached);
      } else {
        viewRoot.innerHTML = `<div class="empty-state"><p class="loading-line">正在从 GitHub 加载正文…</p><p class="text-muted">${escapeHtml(
          post.title
        )}</p></div>`;
        try {
          const url = rawContentUrl(post._githubFile);
          const res = await githubFetch(url);
          if (!res.ok) throw new Error(`HTTP ${res.status}`);
          const text = await res.text();
          saveBodyCache(slug, text);
          applyMarkdownToPost(post, text);
        } catch (e) {
          console.error(e);
          viewRoot.innerHTML = `<div class="empty-state"><p>无法加载该文章正文。</p><p>${escapeHtml(
            e && e.message ? e.message : String(e)
          )}</p><p><a href="#/">返回首页</a></p></div>`;
          detachScrollListeners();
          return;
        }
      }
    }

    if (!String(post.body || "").trim()) {
      viewRoot.innerHTML = `<div class="empty-state"><p>该文章没有可渲染的正文。</p><p>请在 manifest 中为该条配置 <code>file</code> 指向 Markdown 文件。</p><p><a href="#/">返回首页</a></p></div>`;
      detachScrollListeners();
      return;
    }

    const posts = sortedPosts();
    const idx = posts.findIndex((p) => p.slug === slug);
    const prev = posts[idx + 1];
    const next = posts[idx - 1];

    const { html, toc } = parseMarkdown(post.body);
    const mins = readingMinutesFromMarkdown(post.body);
    const metaTags = (post.tags || []).map((t) => escapeHtml(t)).join(" · ");

    const coverHtml = post.cover
      ? `<figure class="article-cover"><img src="${escapeHtml(post.cover)}" alt="" /></figure>`
      : "";

    const tocSidebar = buildTocHtml(toc, "sidebar");
    const tocMobile = buildTocHtml(toc, "mobile");

    viewRoot.innerHTML = `
      ${tocSidebar}
      <article class="article-layout" data-article>
        <header class="article-hero">
          <h1 class="article-hero__title">${escapeHtml(post.title)}</h1>
          <div class="article-hero__meta">
            <span>${escapeHtml(window.blogConfig.blogName)}</span>
            <time datetime="${escapeHtml(post.date)}">${escapeHtml(parseDate(post.date))}</time>
            <span>${mins} 分钟阅读</span>
            ${metaTags ? `<span>${metaTags}</span>` : ""}
          </div>
        </header>
        ${coverHtml}
        <div class="prose">${html}</div>
        ${tocMobile}
        <nav class="post-nav" aria-label="上一篇与下一篇">
          ${
            prev
              ? `<a href="#/post/${encodeURIComponent(prev.slug)}"><div class="post-nav__label">上一篇</div><div class="post-nav__title">${escapeHtml(
                  prev.title
                )}</div></a>`
              : "<span></span>"
          }
          ${
            next
              ? `<a class="post-nav__next" href="#/post/${encodeURIComponent(next.slug)}"><div class="post-nav__label">下一篇</div><div class="post-nav__title">${escapeHtml(
                  next.title
                )}</div></a>`
              : "<span></span>"
          }
        </nav>
      </article>
    `;

    enhanceCodeCopy(viewRoot);
    readingBar.classList.add("is-active");
    attachScrollListeners();
    setupTocScrollSpy(toc);
    requestAnimationFrame(() => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  function setupTocScrollSpy(toc) {
    if (!toc.length) return;
    const links = [...viewRoot.querySelectorAll('.toc-panel a[data-toc-id], .toc-mobile a[href^="#"]')];
    const headings = toc.map((t) => document.getElementById(t.id)).filter(Boolean);
    if (!headings.length) return;

    if (tocObserver) tocObserver.disconnect();
    tocObserver = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        const id = (visible[0] && visible[0].target.id) || headings[0].id;
        links.forEach((a) => {
          const href = a.getAttribute("href") || "";
          const match = href === "#" + id;
          a.classList.toggle("is-active", match);
        });
      },
      { rootMargin: "-20% 0px -70% 0px", threshold: [0, 1] }
    );
    headings.forEach((h) => tocObserver.observe(h));
  }

  function renderAbout() {
    const c = window.blogConfig;
    const ghUser = String(c.github.user || "").trim();
    const ghHref = ghUser ? `https://github.com/${encodeURIComponent(ghUser)}` : "https://github.com";
    viewRoot.innerHTML = `
      <section class="about-card">
        <div class="about-card__avatar" role="img" aria-label="头像占位"></div>
        <h1>${escapeHtml(c.blogName)}</h1>
        <p>${escapeHtml(
          c.blogDescription ||
            "相信文字与留白。这里记录技术、设计与日常的交叉点。"
        )}</p>
        <div class="social-row">
          <a href="${ghHref}" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.48 2 2 6.58 2 12.26c0 4.52 2.87 8.35 6.84 9.7.5.1.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.37-3.37-1.37-.46-1.19-1.13-1.5-1.13-1.5-.92-.64.07-.62.07-.62 1.02.07 1.56 1.07 1.56 1.07.9 1.56 2.34 1.11 2.91.85.09-.67.35-1.11.64-1.37-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.72 0 0 .84-.27 2.75 1.05A9.36 9.36 0 0112 6.82c.85.004 1.705.12 2.52.35 1.9-1.32 2.75-1.05 2.75-1.05.55 1.42.2 2.46.1 2.72.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.8-4.57 5.06.36.32.68.94.68 1.9 0 1.37-.01 2.47-.01 2.8 0 .27.18.59.69.48A10.01 10.01 0 0022 12.26C22 6.58 17.52 2 12 2z"/></svg>
          </a>
          <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="X / Twitter">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 3H21l-7.5 8.66L22 21h-6.44l-4.93-6.42L5.5 21H3l8.02-9.34L2 3h6.56l4.46 5.84L18.244 3zm-2.1 16h1.84L7.93 5H6.02l10.144 14z"/></svg>
          </a>
          <a href="mailto:hello@example.com" aria-label="邮箱">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/></svg>
          </a>
        </div>
      </section>
    `;
    readingBar.classList.remove("is-active");
    detachScrollListeners();
  }

  function renderTags(route) {
    const tags = allTags();
    const active = route.tag || "";
    const cloud = tags
      .map(
        (t) =>
          `<a href="#/tags/${encodeURIComponent(t)}" class="${
            t === active ? "is-active" : ""
          }">${escapeHtml(t)}</a>`
      )
      .join("");

    const inner =
      active && !tags.includes(active)
        ? `<p class="empty-state">没有这个标签。 <a href="#/tags">返回</a></p>`
        : `<h2 class="section-label" style="text-align:center">所有标签</h2>
           <div class="tags-cloud">${cloud}</div>`;

    viewRoot.innerHTML = inner + (active ? "" : "") + `<div id="tag-post-list"></div>`;

    const mount = document.getElementById("tag-post-list");
    if (mount) {
      const posts = sortedPosts().filter((p) => (p.tags || []).includes(active));
      if (active) {
        mount.innerHTML =
          `<p class="filter-bar">包含 <strong>${escapeHtml(
            active
          )}</strong> 的文章</p>` +
          (posts.length
            ? `<div class="post-list">${posts
                .map((p) => {
                  const mins = readingMinutesForPost(p);
                  const thumb = p.cover
                    ? `<div class="post-card__thumb"><img src="${escapeHtml(
                        p.cover
                      )}" alt="" /></div>`
                    : `<div class="post-card__thumb post-card__thumb--gradient"></div>`;
                  return `<a href="#/post/${encodeURIComponent(p.slug)}" class="post-card">
                    ${thumb}
                    <div class="post-card__body">
                      <div class="post-card__meta"><time datetime="${escapeHtml(
                        p.date
                      )}">${escapeHtml(parseDate(p.date))}</time><span>${mins} 分钟阅读</span></div>
                      <h2 class="post-card__title">${escapeHtml(p.title)}</h2>
                      <p class="post-card__excerpt">${escapeHtml(p.excerpt || "")}</p>
                    </div>
                  </a>`;
                })
                .join("")}</div>`
            : `<p class="empty-state">该标签下暂无文章。</p>`);
      } else {
        mount.innerHTML = "";
      }
    }

    readingBar.classList.remove("is-active");
    detachScrollListeners();
  }

  function detachScrollListeners() {
    if (scrollHandler) {
      window.removeEventListener("scroll", scrollHandler);
      scrollHandler = null;
    }
    if (tocObserver) {
      tocObserver.disconnect();
      tocObserver = null;
    }
  }

  function attachScrollListeners() {
    detachScrollListeners();
    const article = viewRoot.querySelector("[data-article]");
    if (!article) return;

    const onScroll = () => {
      const scrollY = window.scrollY;
      const top = article.getBoundingClientRect().top + scrollY;
      const height = article.offsetHeight;
      const viewH = window.innerHeight;
      const end = top + height - viewH;
      const denom = Math.max(end - top, 1);
      let pct = ((scrollY - top) / denom) * 100;
      pct = Math.min(Math.max(pct, 0), 100);
      readingBar.style.width = Math.round(pct) + "%";

      const showTop = scrollY > viewH * 0.85;
      backToTop.classList.toggle("is-visible", showTop);
    };

    scrollHandler = onScroll;
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  function render() {
    const route = parseHash();
    setNavActive(route);

    const run = async () => {
      if (route.name === "home") renderHome();
      else if (route.name === "post") await renderPostAsync(route.slug);
      else if (route.name === "about") renderAbout();
      else if (route.name === "tags") renderTags(route);
      else renderHome();
    };

    if (firstViewRender) {
      firstViewRender = false;
      void Promise.resolve(run()).catch((err) => {
        console.error(err);
        viewRoot.innerHTML = `<div class="empty-state"><p>页面加载出错。</p><p><a href="#/">返回首页</a></p></div>`;
      });
    } else {
      fadeSwap(run);
    }
  }

  /* ---------- theme ---------- */
  function effectiveTheme() {
    const mode = window.blogConfig.themeMode || "auto";
    if (mode === "light") return "light";
    if (mode === "dark") return "dark";
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme() {
    const t = effectiveTheme();
    document.documentElement.setAttribute("data-theme", t);
    themeToggle.setAttribute(
      "aria-label",
      t === "dark" ? "当前为深色，点击切换" : "当前为浅色，点击切换"
    );
  }

  function cycleThemeMode() {
    const order = ["auto", "light", "dark"];
    const cur = window.blogConfig.themeMode || "auto";
    const i = order.indexOf(cur);
    window.blogConfig.themeMode = order[(i + 1) % order.length];
    selectTheme.value = window.blogConfig.themeMode;
    savePrefs({
      ...loadPrefs(),
      themeMode: window.blogConfig.themeMode,
    });
    applyTheme();
  }

  /* ---------- settings ---------- */
  function openSettings(open) {
    settingsPanel.hidden = !open;
  }

  function hydrateSettingsInputs() {
    inputName.value = window.blogConfig.blogName;
    inputDesc.value = window.blogConfig.blogDescription;
    selectTheme.value = window.blogConfig.themeMode || "auto";
    const gh = window.blogConfig.github;
    if (chkGithub) chkGithub.checked = !!gh.enabled;
    if (inputGithubUser) inputGithubUser.value = gh.user || "";
    if (inputGithubRepo) inputGithubRepo.value = gh.repo || "";
    if (inputGithubBranch) inputGithubBranch.value = gh.branch || "main";
    if (inputGithubManifest) inputGithubManifest.value = gh.manifestPath || "content/manifest.json";
    if (inputGithubToken) {
      inputGithubToken.value = "";
      inputGithubToken.placeholder = loadPrefs().githubToken
        ? "留空则保留已保存的 Token"
        : "可选，用于私有仓库";
    }
  }

  function mergePrefsFromStorage() {
    const p = loadPrefs();
    if (p.blogName) window.blogConfig.blogName = p.blogName;
    if (p.blogDescription) window.blogConfig.blogDescription = p.blogDescription;
    if (p.themeMode && ["auto", "light", "dark"].includes(p.themeMode)) {
      window.blogConfig.themeMode = p.themeMode;
    }
    if (p.heroHighlight) window.blogConfig.heroHighlight = p.heroHighlight;
    if (p.github && typeof p.github === "object") {
      window.blogConfig.github = Object.assign({}, window.blogConfig.github, {
        enabled: !!p.github.enabled,
        user: typeof p.github.user === "string" ? p.github.user : "",
        repo: typeof p.github.repo === "string" ? p.github.repo : "",
        branch:
          typeof p.github.branch === "string" && p.github.branch.trim()
            ? p.github.branch.trim()
            : window.blogConfig.github.branch,
        manifestPath:
          typeof p.github.manifestPath === "string" && p.github.manifestPath.trim()
            ? p.github.manifestPath.trim()
            : window.blogConfig.github.manifestPath,
      });
    }
  }

  /* ---------- events ---------- */
  window.addEventListener("hashchange", render);

  themeToggle.addEventListener("click", cycleThemeMode);

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if ((window.blogConfig.themeMode || "auto") === "auto") applyTheme();
  });

  burger.addEventListener("click", () => {
    const open = burger.getAttribute("aria-expanded") === "true";
    burger.setAttribute("aria-expanded", String(!open));
    drawer.hidden = open;
  });

  drawer.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => {
      burger.setAttribute("aria-expanded", "false");
      drawer.hidden = true;
    });
  });

  backToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  settingsToggle.addEventListener("click", () => {
    const hidden = settingsPanel.hidden;
    openSettings(hidden);
    if (hidden) hydrateSettingsInputs();
  });

  btnSave.addEventListener("click", () => {
    window.blogConfig.blogName = inputName.value.trim() || DEFAULT_CONFIG.blogName;
    window.blogConfig.blogDescription =
      inputDesc.value.trim() || DEFAULT_CONFIG.blogDescription;
    window.blogConfig.themeMode = selectTheme.value;
    window.blogConfig.github = {
      enabled: !!(chkGithub && chkGithub.checked),
      user: inputGithubUser ? inputGithubUser.value.trim() : "",
      repo: inputGithubRepo ? inputGithubRepo.value.trim() : "",
      branch: (inputGithubBranch && inputGithubBranch.value.trim()) || "main",
      manifestPath:
        (inputGithubManifest && inputGithubManifest.value.trim()) || "content/manifest.json",
    };

    const prev = loadPrefs();
    const prefs = {
      blogName: window.blogConfig.blogName,
      blogDescription: window.blogConfig.blogDescription,
      themeMode: window.blogConfig.themeMode,
      heroHighlight: window.blogConfig.heroHighlight,
      github: { ...window.blogConfig.github },
    };
    const tok = inputGithubToken ? inputGithubToken.value.trim() : "";
    if (tok) prefs.githubToken = tok;
    else if (prev.githubToken) prefs.githubToken = prev.githubToken;

    savePrefs(prefs);

    void loadBlogDataSource().then(() => {
      applyConfigToDom();
      applyTheme();
      openSettings(false);
      render();
    });
  });

  btnReset.addEventListener("click", () => {
    window.blogConfig = {
      ...DEFAULT_CONFIG,
      github: { ...DEFAULT_CONFIG.github },
    };
    savePrefs({});
    hydrateSettingsInputs();
    applyConfigToDom();
    applyTheme();
    openSettings(false);
    void loadBlogDataSource().then(() => render());
  });

  /* ---------- boot ---------- */
  async function bootstrap() {
    mergePrefsFromStorage();
    await loadBlogDataSource();
    applyConfigToDom();
    applyTheme();
    hydrateSettingsInputs();

    if (!location.hash || location.hash === "#") {
      location.replace("#/");
    }

    requestAnimationFrame(() => {
      mainEl.scrollIntoView({ behavior: "smooth", block: "start" });
    });

    render();
  }

  void bootstrap();
})();
