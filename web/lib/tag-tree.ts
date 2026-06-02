export type TagTrieNode = {
  segment: string;
  /** 叶子对应完整标签，用于跳转 /tags/[tag] */
  fullTag: string | null;
  children: TagTrieNode[];
};

/** 用标签里的 `/` 或 `／` 拆成多级树，例如 `雅思/口语`；每级节点均可跳转 */
export function buildTagTrie(tags: string[]): TagTrieNode[] {
  const root: TagTrieNode[] = [];

  for (const tag of tags) {
    const parts = tag.split(/[/／]/).map((s) => s.trim()).filter(Boolean);
    if (!parts.length) continue;
    let level = root;
    let path = "";
    for (let i = 0; i < parts.length; i++) {
      const seg = parts[i];
      path = path ? `${path}/${seg}` : seg;
      let node = level.find((n) => n.segment === seg);
      if (!node) {
        node = { segment: seg, fullTag: path, children: [] };
        level.push(node);
      } else if (!node.fullTag) {
        node.fullTag = path;
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
