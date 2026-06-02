import type { PostMeta } from "@/lib/posts";

export type PostGroup = {
  name: string;
  /** 用于跳转 /tags/[tag]；中间节点为路径前缀 */
  fullTag: string;
  posts: PostMeta[];
  children: PostGroup[];
};

function splitTagPath(tag: string): string[] {
  return tag.split(/[/／]/).map((s) => s.trim()).filter(Boolean);
}

export function primaryTag(post: PostMeta): string {
  return post.tags[0]?.trim() || "未分类";
}

/** 标签页筛选：精确匹配或子标签（前缀） */
export function tagMatchesFilter(postTags: string[], filter: string): boolean {
  const f = filter.trim();
  if (!f) return false;
  return postTags.some((t) => {
    const tag = t.trim();
    return tag === f || tag.startsWith(`${f}/`) || tag.startsWith(`${f}／`);
  });
}

export function groupPostsByTags(posts: PostMeta[]): PostGroup[] {
  const roots: PostGroup[] = [];

  for (const post of posts) {
    const parts = splitTagPath(primaryTag(post));
    if (!parts.length) {
      ensureLeaf(roots, ["未分类"]).posts.push(post);
      continue;
    }

    let level = roots;
    let path = "";
    for (let i = 0; i < parts.length; i++) {
      const seg = parts[i];
      path = path ? `${path}/${seg}` : seg;
      const isLeaf = i === parts.length - 1;
      let node = level.find((n) => n.name === seg);
      if (!node) {
        node = { name: seg, fullTag: path, posts: [], children: [] };
        level.push(node);
      }
      if (isLeaf) node.posts.push(post);
      level = node.children;
    }
  }

  const sortRec = (nodes: PostGroup[]) => {
    nodes.sort((a, b) => a.name.localeCompare(b.name, "zh-CN"));
    for (const n of nodes) {
      n.posts.sort((a, b) =>
        (b.updated || b.date || "").localeCompare(a.updated || a.date || "", "zh-CN")
      );
      sortRec(n.children);
    }
  };
  sortRec(roots);
  return roots;
}

function ensureLeaf(roots: PostGroup[], parts: string[]): PostGroup {
  let level = roots;
  let path = "";
  let node: PostGroup | undefined;
  for (let i = 0; i < parts.length; i++) {
    const seg = parts[i];
    path = path ? `${path}/${seg}` : seg;
    node = level.find((n) => n.name === seg);
    if (!node) {
      node = { name: seg, fullTag: path, posts: [], children: [] };
      level.push(node);
    }
    level = node.children;
  }
  return node!;
}
