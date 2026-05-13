import PostReadingMode from "@/components/PostReadingMode";

export default function PostSlugLayout({ children }: { children: React.ReactNode }) {
  return <PostReadingMode>{children}</PostReadingMode>;
}
