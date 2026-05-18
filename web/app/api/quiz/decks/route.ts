import { listVocabDecks } from "@/lib/vocab";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const decks = await listVocabDecks();
    return Response.json({ decks });
  } catch (e) {
    console.error("[quiz/decks]", e);
    return Response.json({ error: "无法读取词库" }, { status: 500 });
  }
}
