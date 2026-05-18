import fs from "fs/promises";
import path from "path";

export type CardProgress = {
  correct: number;
  wrong: number;
  streak: number;
  lastReviewed?: string;
};

export type QuizProgressFile = {
  version: 1;
  byCard: Record<string, CardProgress>;
};

const EMPTY: QuizProgressFile = { version: 1, byCard: {} };

function getDataDir(): string {
  if (process.env.QUIZ_DATA_DIR) return process.env.QUIZ_DATA_DIR;
  return path.join(process.cwd(), "data");
}

function progressPath(): string {
  return path.join(getDataDir(), "quiz-progress.json");
}

export function checkQuizWriteAuth(req: Request): boolean {
  const secret = process.env.QUIZ_SECRET?.trim();
  if (!secret) return true;
  const auth = req.headers.get("authorization");
  if (!auth?.startsWith("Bearer ")) return false;
  return auth.slice(7) === secret;
}

export async function readProgress(): Promise<QuizProgressFile> {
  try {
    const raw = await fs.readFile(progressPath(), "utf8");
    const j = JSON.parse(raw) as QuizProgressFile;
    if (j?.version === 1 && j.byCard) return j;
    return { ...EMPTY };
  } catch {
    return { ...EMPTY };
  }
}

export async function writeProgress(data: QuizProgressFile): Promise<void> {
  const dir = getDataDir();
  await fs.mkdir(dir, { recursive: true });
  await fs.writeFile(progressPath(), JSON.stringify(data, null, 2), "utf8");
}

export async function recordReview(cardId: string, correct: boolean): Promise<CardProgress> {
  const file = await readProgress();
  const prev = file.byCard[cardId] || { correct: 0, wrong: 0, streak: 0 };
  const next: CardProgress = {
    correct: prev.correct + (correct ? 1 : 0),
    wrong: prev.wrong + (correct ? 0 : 1),
    streak: correct ? prev.streak + 1 : 0,
    lastReviewed: new Date().toISOString(),
  };
  file.byCard[cardId] = next;
  await writeProgress(file);
  return next;
}

export async function getProgressSummary(): Promise<{
  totalReviews: number;
  cardsTouched: number;
  byCard: Record<string, CardProgress>;
}> {
  const file = await readProgress();
  let totalReviews = 0;
  for (const p of Object.values(file.byCard)) {
    totalReviews += p.correct + p.wrong;
  }
  return {
    totalReviews,
    cardsTouched: Object.keys(file.byCard).length,
    byCard: file.byCard,
  };
}
