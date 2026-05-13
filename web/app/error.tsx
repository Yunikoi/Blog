"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="wrap" style={{ paddingTop: "3rem" }}>
      <h1>页面出错了</h1>
      <p style={{ color: "var(--muted)" }}>部署到 Vercel 时常见原因是未同步到 <code>content</code> 或某篇 Markdown 格式异常。请查看 Vercel 该次部署的 Function Logs。</p>
      <pre
        style={{
          fontSize: "0.85rem",
          overflow: "auto",
          padding: "1rem",
          background: "var(--border)",
          borderRadius: "8px",
        }}
      >
        {error.message}
      </pre>
      <p>
        <button type="button" onClick={() => reset()} style={{ marginRight: "1rem" }}>
          重试
        </button>
        <a href="/">返回首页</a>
      </p>
    </div>
  );
}
