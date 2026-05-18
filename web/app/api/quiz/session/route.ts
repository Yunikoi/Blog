import { buildChoices, loadDeckCards, shuffle } from "@/lib/vocab";
import { readProgress } from "@/lib/quiz-progress";

export const dynamic = "force-dynamic";

export type QuizSessionItem = {
  id: string;
  term: string;
  definition: string;
  choices: string[];
  deckSlug: string;
};

/** GET ?deck=slug&count=10&mode=term-to-def */
export async function GET(req: Request) {
  const url = new URL(req.url);
  const deck = url.searchParams.get("deck")?.trim();
  const count = Math.min(50, Math.max(1, Number(url.searchParams.get("count")) || 10));
  const mode = url.searchParams.get("mode") || "term-to-def";

  if (!deck) {
    return Response.json({ error: "请指定 deck 参数（文章 slug）" }, { status: 400 });
  }

  try {
    const cards = await loadDeckCards(deck);
    if (!cards.length) {
      return Response.json({ error: "该文章未解析到词条（需 `#### 词：释义` 格式）" }, { status: 404 });
    }

    const progress = await readProgress();
    const pool = shuffle(cards);

    const prioritized = [
      ...pool.filter((c) => {
        const p = progress.byCard[c.id];
        return !p || p.wrong > p.correct;
      }),
      ...pool.filter((c) => {
        const p = progress.byCard[c.id];
        return p && p.wrong <= p.correct;
      }),
    ];

    const picked = prioritized.slice(0, count);
    const items: QuizSessionItem[] = picked.map((card) => {
      const choices =
        mode === "def-to-term" ? buildChoices(card, cards, 4, "term") : buildChoices(card, cards, 4, "definition");

      return {
        id: card.id,
        term: card.term,
        definition: card.definition,
        choices,
        deckSlug: card.deckSlug,
      };
    });

    return Response.json({
      deck,
      mode,
      totalInDeck: cards.length,
      items,
    });
  } catch (e) {
    console.error("[quiz/session]", e);
    return Response.json({ error: "生成练习失败" }, { status: 500 });
  }
}
