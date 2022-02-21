from jikanpy import Jikan, AioJikan


async def get_anime_list(name):
    titles = []
    id_list = []
    async with AioJikan() as animelist:
        anime = animelist.search("anime", name)
    if anime:
        results = anime["results"]
        if results:
            for result in results:
                titles.append(result["title"])
                id_list.append(result["mal_id"])
            return titles, id_list
        else:
            return None, None

async def get_anime_by_id(id, mode="msg"):
    async with AioJikan() as animelist:
        anime = animelist.anime(id)
    if anime:
        img_url = anime["image_url"]

        title = anime["title"]
        msg = f"<b>Title :</b> <code>{title}</code>\n\n"
        msg += f"<b>Known as :</b> <code>{anime['title']}</code>\n\n"
        msg += f"<b>Type :</b> <code>{anime['type']}</code>\n\n"
        msg += f"<b>Episodes :</b> <code>{anime['episodes']}</code>\n\n"
        msg += f"<b>Status :</b> <code>{anime['status']}</code>\n\n"

        short_desc = f"Type: {anime['type']} Status: {anime['status']}"
        try:
            msg += f"<b>Score :</b> <code>{anime['score']}</code>\n\n"
        except:
            pass
        try:
            msg += f"<b>Source :</b> <code>{anime['source']}</code>\n\n"
        except:
            pass
        try:
            msg += f"<b>Aired :</b> <code>{anime['aired']['string']}</code>\n\n"
        except:
            pass
        try:
            desc = anime["synopsis"]
            if len(desc) > 750:
                desc = desc[:750] + "..."
            msg += f"<b>Description :</b>\n<code>{desc}</code>\n\n"
        except:
            pass
        if mode == "msg":
            try:
                trailer = anime["trailer_url"]
            except:
                trailer = None
            return img_url, msg, trailer
        else:
            return img_url, msg, title, short_desc

async def get_all_details(name):
    anime = None
    id_list = []
    titles = []
    img_list = []
    msg_list = []
    desc_list = []
    async with AioJikan() as aio_mal:
        anime = await aio_mal.search("anime", name)
        print(anime)
    if anime:
        results = anime["results"]
        if results:
            for result in results:
                id_list.append(result["mal_id"])
        for a_id in id_list:
            img, msg, title, short_desc = await get_anime_by_id(a_id, mode="aio")
            img_list.append(img)
            msg_list.append(msg)
            titles.append(title)
            desc_list.append(short_desc)
        return img_list, msg_list, titles, desc_list







