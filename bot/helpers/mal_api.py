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
