/** 客户端 / 服务端均可用的纯函数（勿引入 fs） */

export type VocabCard = {
  id: string;
  deckSlug: string;
  deckTitle: string;
  term: string;
  definition: string;
};

export function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function buildChoices(
  correct: VocabCard,
  pool: VocabCard[],
  count = 4,
  field: "definition" | "term" = "definition"
): string[] {
  const pick = (c: VocabCard) => (field === "term" ? c.term : c.definition);
  const distractors = shuffle(pool.filter((c) => c.id !== correct.id))
    .slice(0, count - 1)
    .map(pick);
  const choices = shuffle([pick(correct), ...distractors]);
  while (choices.length < count && pool.length > choices.length) {
    const extra = pool.find((c) => c.id !== correct.id && !choices.includes(pick(c)));
    if (!extra) break;
    choices.push(pick(extra));
  }
  return shuffle(choices.slice(0, count));
}
