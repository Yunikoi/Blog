import type { ReactNode } from "react";

export default function LayoutChrome({ children }: { children: ReactNode }) {
  return <div className="layout-chrome">{children}</div>;
}
