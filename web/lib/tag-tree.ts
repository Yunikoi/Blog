export type TagTrieNode = {
  segment: string;
  /** 叶子对应完整标签，用于跳转 /tags/[tag] */
  fullTag: string | null;
  children: TagTrieNode[];
};

/** 用标签里的 `/` 或 `／` 拆成多级树，例如 `雅思/口语` */
export function buildTagTrie(tags: string[]): TagTrieNode[] {
  const root: TagTrieNode[] = [];

  for (const tag of tags) {
    const parts = tag.split(/[/／]/).map((s) => s.trim()).filter(Boolean);
    if (!parts.length) continue;
    let level = root;
    for (let i = 0; i < parts.length; i++) {
      const seg = parts[i];
      let node = level.find((n) => n.segment === seg);
      if (!node) {
        node = { segment: seg, fullTag: null, children: [] };
        level.push(node);
      }
      if (i === parts.length - 1) {
        node.fullTag = tag;
      }
      level = node.children;
    }
  }

  const sortRec = (nodes: TagTrieNode[]) => {
    nodes.sort((a, b) => a.segment.localeCompare(b.segment, "zh-CN"));
    nodes.forEach((n) => sortRec(n.children));
  };
  sortRec(root);
  return root;
}
