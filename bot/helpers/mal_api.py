from jikanpy import Jikan

animelist = Jikan()

def get_anime_list(name):
    titles = []
    id_list = []
    try:
        anime = animelist.search("anime", name)
    except:
        return None
    if anime:
        results = anime["results"]
        if results:
            for result in results:
                titles.append(result["title"])
                id_list.append(result["mal_id"])
            return titles, id_list
        else:
            return None, None

def get_anime_by_id(id):
    try:
        anime = animelist.anime(id)
    except:
        return None
    if anime:
        img_url = anime["image_url"]
        
        msg = f"<b>Title :</b> <code>{anime['title_english']}</code>\n\n"
        msg += f"<b>Known as :</b> <code>{anime['title']}</code>\n\n"
        msg += f"<b>Type :</b> <code>{anime['type']}</code>\n\n"
        msg += f"<b>Episodes :</b> <code>{anime['episodes']}</code>\n\n"
        msg += f"<b>Status :</b> <code>{anime['status']}</code>\n\n"

        return img_url, msg

