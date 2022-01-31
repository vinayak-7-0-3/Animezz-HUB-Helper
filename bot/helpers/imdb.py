import requests
from bot import FOOTER

imdb_query = "https://api.abirhasan.wtf/imdb/search?query="
imdb_link = "https://api.abirhasan.wtf/imdb/get?link="

async def get_info(query):
    titles = []
    msgs = []
    photos = []

    data = requests.get(f"{imdb_query}{query}").json()
    for item in data.get("data"):
        try:
            title = item.get("title")
        except:
            title = None
        try:
            link = item.get("imdb_link")
        except:
            link = None
        try:
            photo = item.get("thumbnail")
        except:
            photo = None
            
        data2 = requests.get(imdb_link + link).json()
        story_line = data2.get("story_line")
        director = data2.get("directors")
        release_date = data2.get("release")
        if " (" in release_date:
            release_date = release_date.split(" (")[0]
        rating = data2.get("rating")

        msg = f"<b>Title :</b> <code>{title}</code>\n\n"
        msg += f"<b>IMDB Rating :</b> <code>{rating}</code>\n\n"
        msg += f"<b>Release :</b> <code>{release_date}</code>\n\n"
        msg += f"<b>Director :</b> <code>{director}</code>\n\n"
        msg += f"<b>Storyline :</b> <code>{story_line}</code>"

        if FOOTER:
            msg += f"\n\n{FOOTER}"
        
        titles.append(title)
        msgs.append(msg)
        photos.append(photo)

    return msgs, titles, photos

"""async def get_photo(link, title):
    response = requests.get(link)
    file = open(f"{DL_PATH}/{title}.jpg", "wb")
    file.write(response.content)
    file.close()"""




