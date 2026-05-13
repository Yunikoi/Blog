import { listPublicMusicTracks } from "@/lib/music-public";

export const dynamic = "force-dynamic";

export async function GET() {
  const tracks = await listPublicMusicTracks();
  return Response.json(tracks);
}
