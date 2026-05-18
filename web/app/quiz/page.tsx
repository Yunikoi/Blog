import VocabQuiz from "@/components/VocabQuiz";

export const metadata = {
  title: "背单词",
};

export default function QuizPage() {
  return (
    <div className="wrap quiz-page">
      <h1 className="page-title">背单词</h1>
      <VocabQuiz />
      <section className="quiz-hint" aria-label="使用说明">
        <h2 className="quiz-hint__title">任意网络打开即可</h2>
        <p className="quiz-muted">
          将 <code>web</code> 文件夹部署到 Vercel（根目录选 <code>web</code>），手机浏览器访问{" "}
          <strong>你的域名/quiz</strong> 即可，无需与电脑同一 Wi‑Fi。更新笔记后重新部署即可同步词库。
        </p>
      </section>
    </div>
  );
}
