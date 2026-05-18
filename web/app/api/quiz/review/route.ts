import { checkQuizWriteAuth, getProgressSummary, recordReview } from "@/lib/quiz-progress";

export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  if (!checkQuizWriteAuth(req)) {
    return Response.json({ error: "未授权（需配置 QUIZ_SECRET 并在请求头携带 Bearer）" }, { status: 401 });
  }

  try {
    const body = (await req.json()) as { cardId?: string; correct?: boolean };
    const cardId = body.cardId?.trim();
    if (!cardId) {
      return Response.json({ error: "缺少 cardId" }, { status: 400 });
    }

    const progress = await recordReview(cardId, Boolean(body.correct));
    return Response.json({ ok: true, progress });
  } catch (e) {
    console.error("[quiz/review]", e);
    return Response.json({ error: "保存进度失败" }, { status: 500 });
  }
}

export async function GET() {
  try {
    const summary = await getProgressSummary();
    return Response.json(summary);
  } catch (e) {
    console.error("[quiz/review GET]", e);
    return Response.json({ error: "读取进度失败" }, { status: 500 });
  }
}
