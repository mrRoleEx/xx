import re
from dataclasses import replace

import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.client import Client
from pyrogram.types import InlineKeyboardButton as ikb
from pyrogram.types import InlineKeyboardMarkup as ikm


bot = Client("bot", bot_token="5744404637:AAFs-pq3UL34jqW1nti4eP8KOC8kf4Ncs_Q",
             api_id=1712043, api_hash="965c994b615e2644670ea106fd31daaf")


async def getmovie(url):
    response = requests.get(url)
    html = response.content.decode()
    soup = BeautifulSoup(html, "html.parser")
    link = soup.find_all("div", attrs={"class": "A2"})
    array = []
    #print(url)
    for linnk in link:
        array.append(linnk.find("a").get("href"))
        if len(array) == 10:
            break
    result = array[:11]
    w = "https://filmy4wap.dev".join(result)
    g = "https://filmy4wap.dev" + w
    y = g.split(".html")
    url2 = y[0]
    res = requests.get(url2)
    html2 = res.content.decode()
    soup2 = BeautifulSoup(html2, "html.parser")


    for linkk in soup2.find_all(
        "a", attrs={"href": re.compile("^/page-downloading-page/")}
    ):
        break
    reallink = linkk.get("href")
    t = "".join(reallink)
    k = "https://filmy4wap.dev" + t

    url3 = k
    res2 = requests.get(url3)
    html3 = res2.content.decode()
    soup3 = BeautifulSoup(html3, "html.parser")
    for linkk1 in soup3.find_all(
        "a", attrs={"href": re.compile("^https://link2me.xyz/")}
    ):
        break
    jaadu = linkk1.get("href")
    url4 = jaadu
    res3 = requests.get(url4)
    html4 = res3.content.decode()
    soup4 = BeautifulSoup(html4, "html.parser")
    super = soup4.find_all("div", attrs={"class": "dlink dl"})
    super6 = soup4.find_all("div", class_="dll")

    xxlink = []
    for strrr in super6:
        xxlink.append(strrr.text)

    str5 = "\n"
    #print(xxlink)
    for i in xxlink:
        str5 += i
        if str5 == "":
            str5 = "No link found"
            break

    po = str5.replace(",", "\n")
    poo = po.replace("] ", "\n")
    pooo = poo.replace("]", "")
    poooo = pooo.replace("[", "!! ")
    #print(poooo)

    global resse
    resse = []

    for linkk2 in super:
        resse.append(linkk2.find("a").get("href"))
    # #print (resse[1])
    if resse == [9]:
        resse.append("No link found")

    global finlink
    finlink = resse #Links will be stored in Finlink

    maxx = len(resse)
    
    return my_buttons(resse,xxlink,2)


@bot.on_message(filters.command("start"))
def start(bot, message):
    bot.send_message(
        message.chat.id,
        "Welcome to MovieSearcher Bot\n Use this bot to search movies \n\n ex:- /Search moviename \n\nnote :- We didn't Allow piracy \nBot use only Webscrapping algo. ",
    )
    #create a button for finlink using for loop


def my_buttons(finlink,xxlink,n):
    from pyrogram.types import InlineKeyboardMarkup as ikm
    from pyrogram.types import InlineKeyboardButton as ikb
    V=finlink
    name=xxlink
    
    
    NV1=[]
    num=0
    N=n
    for x in range(len(V)//N):
      NV2=[]
      for y in range(N):
        NV2.append(ikb(name[num][9:],url=V[y+N*x]))
        #
        num+=1
      NV1.append(NV2)
      
    NV2=[]
    for y in V[(len(V)//N)*N:]:
      NV2.append(ikb(name[num][9:],url=y))
      
      num+=1
    NV1.append(NV2)
    print(ikm(NV1))
    return ikm(NV1)



@bot.on_message(filters.command(["search"]))
async def sm(bot, message):
    await bot.send_message(message.chat.id, "searching.......")
    #button = ikb("Download", url=resse[1])

#await bot.send_message(message.chat.id, "Download", reply_markup=ikm([[button]]))
    movie_name = " ".join(message.command[1:])
    url = "https://filmy4wap.dev/site-1.html?to-search=" + movie_name
    resuult = await getmovie(url)
    #await bot.send_message(message.chat.id, "Results of : " + "" + movie_name + "")
    # create a button using for loop for resse list

    await bot.send_message(message.chat.id,caption="Results of : " + "" + movie_name + "",reply_markup=resuult)
    #await bot.send_message(message.chat.id, resuult)


if __name__ == "__main__":
    bot.run(print("bot started"))
