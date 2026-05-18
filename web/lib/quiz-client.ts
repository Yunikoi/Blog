import type { VocabCard } from "@/lib/vocab-core";
import { buildChoices, shuffle } from "@/lib/vocab-core";

export type QuizBankDeck = {
  slug: string;
  title: string;
  cards: VocabCard[];
};

export type QuizBank = {
  version: number;
  generatedAt: string;
  decks: QuizBankDeck[];
};

export type QuizMode = "term-to-def" | "def-to-term";

export type SessionItem = {
  id: string;
  term: string;
  definition: string;
  choices: string[];
  deckSlug: string;
};

export type CardProgress = {
  correct: number;
  wrong: number;
  streak: number;
  lastReviewed?: string;
};

const BANK_URL = "/quiz-bank.json";
const PROGRESS_KEY = "quiz-progress-v1";

export async function loadQuizBank(): Promise<QuizBank> {
  const r = await fetch(BANK_URL, { cache: "no-store" });
  if (!r.ok) throw new Error("词库文件未找到，请在 web 目录执行 npm run build");
  return r.json() as Promise<QuizBank>;
}

export function listDecksFromBank(bank: QuizBank) {
  return bank.decks.map((d) => ({ slug: d.slug, title: d.title, count: d.cards.length }));
}

function readProgress(): Record<string, CardProgress> {
  if (typeof localStorage === "undefined") return {};
  try {
    const raw = localStorage.getItem(PROGRESS_KEY);
    if (!raw) return {};
    const j = JSON.parse(raw) as { byCard?: Record<string, CardProgress> };
    return j.byCard || {};
  } catch {
    return {};
  }
}

export function recordProgressLocal(cardId: string, correct: boolean): void {
  if (typeof localStorage === "undefined") return;
  const byCard = readProgress();
  const prev = byCard[cardId] || { correct: 0, wrong: 0, streak: 0 };
  byCard[cardId] = {
    correct: prev.correct + (correct ? 1 : 0),
    wrong: prev.wrong + (correct ? 0 : 1),
    streak: correct ? prev.streak + 1 : 0,
    lastReviewed: new Date().toISOString(),
  };
  localStorage.setItem(PROGRESS_KEY, JSON.stringify({ version: 1, byCard }));
}

export function buildQuizSession(
  deck: QuizBankDeck,
  count: number,
  mode: QuizMode
): SessionItem[] {
  const cards = deck.cards;
  const progress = readProgress();

  const prioritized = [
    ...shuffle(cards.filter((c) => {
      const p = progress[c.id];
      return !p || p.wrong > p.correct;
    })),
    ...shuffle(cards.filter((c) => {
      const p = progress[c.id];
      return p && p.wrong <= p.correct;
    })),
  ];

  const picked = prioritized.slice(0, count);
  const field = mode === "def-to-term" ? "term" : "definition";

  return picked.map((card) => ({
    id: card.id,
    term: card.term,
    definition: card.definition,
    choices: buildChoices(card, cards, 4, field),
    deckSlug: card.deckSlug,
  }));
}
