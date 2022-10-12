
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
# text = input('type movie name:- ')
# url = 'https://vegamovies.baby/?s=' + text

bot = Client("bot", bot_token="5744404637:AAFs-pq3UL34jqW1nti4eP8KOC8kf4Ncs_Q",
             api_id=1712043, api_hash="965c994b615e2644670ea106fd31daaf")
#a = input("Enter the message: ")


async def get_movies(url):
    response = requests.get(url)
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')
    n = soup.find("div", {"class": "blog-items blog-items-control site__row movie-grid"})
    s = n.find_all('a')

    array = []
    for linnk in s:
        array.append(linnk.get('href'))
        if len(array) == 6:
            break

    result = array[:5]
    # print(result)
    return "\n".join(result)


@bot.on_message(filters.command(["/","start"]))
async def start(bot, message):
    await bot.send_message(message.chat.id, "Use this bot to search movies\nexample : /search moviename \n BOT Made by @IRoleEx")
 
@bot.on_message(filters.command(['/',"search"]))
async def sm(bot,message):
    movie_name = " ".join(message.command[1:])
    url = 'https://vegamovies.baby/?s=' + movie_name
    print(url)
    results = await get_movies(url)
    await message.reply_text("Searching.. \n\n BY Mr.XED")
    await message.reply(results)


if __name__=="__main__":
    bot.run()
