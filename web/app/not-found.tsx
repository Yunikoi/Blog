import Link from "next/link";

export default function NotFound() {
  return (
    <div className="wrap">
      <h1>未找到文章</h1>
      <p>
        <Link href="/">返回首页</Link>
      </p>
    </div>
  );
}
