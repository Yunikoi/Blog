"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  const digest = error.digest;
  const isGenericProduction =
    typeof error.message === "string" &&
    error.message.includes("omitted in production builds");

  return (
    <div className="wrap" style={{ paddingTop: "3rem" }}>
      <h1>页面出错了</h1>
      {digest ? (
        <p style={{ color: "var(--muted)" }}>
          错误编号（digest）：<code>{digest}</code> — 在 Vercel 的 <strong>Runtime Logs</strong> 里用该编号或时间点搜索，可看到完整堆栈。
        </p>
      ) : null}
      {isGenericProduction ? (
        <p style={{ color: "var(--muted)" }}>
          当前是 <strong>生产环境</strong>：Next.js 会<strong>故意不向浏览器</strong>输出服务端错误的具体原因（你看到的 “omitted in production…”
          是正常现象）。排查请看 Vercel 后台日志；本地可执行 <code>npm run build</code> 后 <code>npm run start</code> 再打开页面，终端里会打印完整错误。
        </p>
      ) : (
        <p style={{ color: "var(--muted)" }}>
          若已部署到 Vercel，仍建议对照 <strong>Runtime Logs</strong>；常见原因包括 <code>content</code> 未同步、某篇 Markdown / 头信息异常等。
        </p>
      )}
      {!isGenericProduction ? (
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
      ) : null}
      <p style={{ fontSize: "0.9rem" }}>
        日志说明：{" "}
        <a href="https://vercel.com/docs/concepts/observability/runtime-logs" target="_blank" rel="noopener noreferrer">
          Vercel Runtime Logs
        </a>
      </p>
      <p>
        <button type="button" onClick={() => reset()} style={{ marginRight: "1rem" }}>
          重试
        </button>
        <a href="/">返回首页</a>
      </p>
    </div>
  );
}
