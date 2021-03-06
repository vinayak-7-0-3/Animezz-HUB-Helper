import requests
from bot import FOOTER

imdb_query = "https://api.abirhasan.wtf/imdb/search?query="
imdb_link = "https://api.abirhasan.wtf/imdb/get?link="

"""async def get_photo(link, title):
    response = requests.get(link)
    file = open(f"{DL_PATH}/{title}.jpg", "wb")
    file.write(response.content)
    file.close()"""

async def reqLinkID(query):
    id_list = []
    titles = []
    data = requests.get(f"{imdb_query}{query}").json()
    try:
        for i in data.get("data"):
            id_list.append(i.get("imdb_link").replace("https://www.imdb.com/title/", ""))
            titles.append(i.get("title"))
    except:
        id_list.append(None)
        titles.append(None)
    return titles, id_list

async def get_info_from_id(link):
    data = requests.get(imdb_link + link).json()

    title = data.get("title")
    story_line = str(data.get("story_line"))
    director = str(data.get("directors"))
    release_date = str(data.get("release"))
    rating = str(data.get("rating"))

    data2 = requests.get(f"{imdb_query}{title}").json()
    for items in data2.get("data"):
        check_link = items.get("imdb_link")
        if check_link == link:
            photo = items.get("thumbnail")
            break
    
    msg = f"<b>Title :</b> <code>{title}</code>\n\n"
    msg += f"<b>IMDB Rating :</b> <code>{rating}</code>\n\n"
    msg += f"<b>Release :</b> <code>{release_date}</code>\n\n"
    msg += f"<b>Director :</b> <code>{director}</code>\n\n"
    msg += f"<b>Storyline :</b> <code>{story_line}</code>"

    if FOOTER:
        msg += f"\n\n{FOOTER}"

    return msg, photo




