import asyncio
import tracemoepy
import mimetypes
import requests

async def tracemoe_trace(file_path=None, link=None):
    if link:
        async with tracemoepy.AsyncTrace() as tracemoe:
            resp = await tracemoe.search(link, is_url=True)
            content = resp.result[0]
            msg = f"Title: {content.anilist.title.romaji}\n"
            msg += f"Adult: {content.anilist.isAdult}\n"
            msg += f"Episode: {content.episode}\n"
            msg += f"Similarity: {content.similarity*100}\n"
            try:
                video = content.video
            except:
                video = None
    else:
        mt = mimetypes.guess_type(file_path)
        r = requests.post("https://api.trace.moe/search",
            data=open(file_path, "rb"),
            headers={"Content-Type": f"{mt[0]}"}
        ).json()
        msg = f"Title: {r['result'][0]['filename']}\n"
        msg += f"Episode: {r['result'][0]['episode']}\n"
        msg += f"Similarity: {r['result'][0]['similarity']*100}"
        try:
            video = r["result"][0]["video"]
        except:
            video = None
    return msg, video

    
