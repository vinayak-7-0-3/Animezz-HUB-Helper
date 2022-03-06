import asyncio
import tracemoepy

async def tracemoe_trace(file_path):
    async with tracemoepy.AsyncTrace() as tracemoe:
        resp = await tracemoe.search(file_path, upload_file=True)
        content = resp.result[0]
        msg = f"Title: {content.anilist.title.romaji}\n"
        msg += f"Adult: {content.anilist.isAdult}\n"
        msg += f"Episode: {content.episode}\n"
        msg += f"Similarity: {content.similarity*100}\n"
        try:
            video_link = content.video
        except:
            video_link = None
        return msg, video_link
