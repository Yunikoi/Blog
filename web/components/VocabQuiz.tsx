"use client";

import { useCallback, useEffect, useState } from "react";
import {
  buildQuizSession,
  listDecksFromBank,
  loadQuizBank,
  recordProgressLocal,
  type QuizBank,
  type QuizMode,
  type SessionItem,
} from "@/lib/quiz-client";

type Deck = { slug: string; title: string; count: number };

export default function VocabQuiz() {
  const [bank, setBank] = useState<QuizBank | null>(null);
  const [decks, setDecks] = useState<Deck[]>([]);
  const [deck, setDeck] = useState("");
  const [mode, setMode] = useState<QuizMode>("term-to-def");
  const [count, setCount] = useState(10);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");

  const [items, setItems] = useState<SessionItem[]>([]);
  const [index, setIndex] = useState(0);
  const [phase, setPhase] = useState<"pick" | "quiz" | "done">("pick");
  const [picked, setPicked] = useState<string | null>(null);
  const [score, setScore] = useState({ correct: 0, total: 0 });

  useEffect(() => {
    loadQuizBank()
      .then((b) => {
        setBank(b);
        const list = listDecksFromBank(b);
        setDecks(list);
        if (list.length) setDeck(list[0].slug);
      })
      .catch((e) => setErr(e instanceof Error ? e.message : "加载词库失败"))
      .finally(() => setLoading(false));
  }, []);

  const startSession = useCallback(() => {
    if (!bank || !deck) return;
    const d = bank.decks.find((x) => x.slug === deck);
    if (!d) {
      setErr("词库不存在");
      return;
    }
    setErr("");
    const session = buildQuizSession(d, count, mode);
    if (!session.length) {
      setErr("没有抽到题目");
      return;
    }
    setItems(session);
    setIndex(0);
    setPicked(null);
    setScore({ correct: 0, total: 0 });
    setPhase("quiz");
  }, [bank, deck, count, mode]);

  const current = items[index];
  const answerText = mode === "def-to-term" ? current?.term : current?.definition;
  const promptText = mode === "def-to-term" ? current?.definition : current?.term;

  const onChoose = (choice: string) => {
    if (!current || picked) return;
    setPicked(choice);
    const ok = choice === answerText;
    setScore((s) => ({ correct: s.correct + (ok ? 1 : 0), total: s.total + 1 }));
    recordProgressLocal(current.id, ok);
  };

  const next = () => {
    if (index + 1 >= items.length) {
      setPhase("done");
      return;
    }
    setIndex((i) => i + 1);
    setPicked(null);
  };

  if (loading && !decks.length) {
    return <p className="quiz-muted">正在加载词库…</p>;
  }

  return (
    <div className="vocab-quiz">
      {phase === "pick" && (
        <>
          <p className="quiz-lead">
            打开网站即可练习。词库随博客文章发布；学习进度保存在本机浏览器，换设备需重新积累。
          </p>

          {decks.length === 0 ? (
            <p className="quiz-err">{err || "暂无词库。文章需使用 `#### 词：释义` 格式。"}</p>
          ) : (
            <div className="quiz-form">
              <label className="quiz-field">
                <span>词库（文章）</span>
                <select value={deck} onChange={(e) => setDeck(e.target.value)}>
                  {decks.map((d) => (
                    <option key={d.slug} value={d.slug}>
                      {d.title}（{d.count} 词）
                    </option>
                  ))}
                </select>
              </label>

              <label className="quiz-field">
                <span>模式</span>
                <select value={mode} onChange={(e) => setMode(e.target.value as QuizMode)}>
                  <option value="term-to-def">看词选义</option>
                  <option value="def-to-term">看义选词</option>
                </select>
              </label>

              <label className="quiz-field">
                <span>题数</span>
                <select value={count} onChange={(e) => setCount(Number(e.target.value))}>
                  {[5, 10, 15, 20, 30].map((n) => (
                    <option key={n} value={n}>
                      {n}
                    </option>
                  ))}
                </select>
              </label>

              <button type="button" className="quiz-btn quiz-btn--primary" onClick={startSession}>
                开始练习
              </button>
            </div>
          )}

          {err && decks.length > 0 ? <p className="quiz-err">{err}</p> : null}
        </>
      )}

      {phase === "quiz" && current ? (
        <div className="quiz-session">
          <p className="quiz-progress">
            {index + 1} / {items.length} · 已对 {score.correct}
          </p>
          <p className="quiz-prompt-label">{mode === "def-to-term" ? "释义" : "单词 / 短语"}</p>
          <h2 className="quiz-prompt">{promptText}</h2>
          <ul className="quiz-choices">
            {current.choices.map((c, i) => {
              const chosen = picked === c;
              const isAnswer = c === answerText;
              let cls = "quiz-choice";
              if (picked) {
                if (isAnswer) cls += " quiz-choice--correct";
                else if (chosen) cls += " quiz-choice--wrong";
              }
              return (
                <li key={`${current.id}-${i}-${c.slice(0, 24)}`}>
                  <button type="button" className={cls} disabled={Boolean(picked)} onClick={() => onChoose(c)}>
                    {c}
                  </button>
                </li>
              );
            })}
          </ul>
          {picked ? (
            <div className="quiz-after">
              {picked !== answerText ? (
                <p className="quiz-answer-hint">
                  正确答案：<strong>{answerText}</strong>
                </p>
              ) : null}
              <button type="button" className="quiz-btn quiz-btn--primary" onClick={next}>
                {index + 1 >= items.length ? "查看结果" : "下一题"}
              </button>
            </div>
          ) : null}
        </div>
      ) : null}

      {phase === "done" ? (
        <div className="quiz-done">
          <h2>本轮完成</h2>
          <p className="quiz-score">
            {score.correct} / {score.total} 正确
          </p>
          <button type="button" className="quiz-btn quiz-btn--primary" onClick={() => setPhase("pick")}>
            再练一轮
          </button>
        </div>
      ) : null}
    </div>
  );
}
