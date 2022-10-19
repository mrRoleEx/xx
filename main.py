from dataclasses import replace
import re

import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.client import Client
from telegram import InputContactMessageContent

# text = input('type movie name:- ')
# url = 'https://vegamovies.baby/?s=' + text

bot = Client(
    "bot",
    bot_token="5744404637:AAFs-pq3UL34jqW1nti4eP8KOC8kf4Ncs_Q",
    api_id=1712043,
    api_hash="965c994b615e2644670ea106fd31daaf",
)
# a = input("Enter the message: ")


# text = input('type movie name:- ')
# url = 'https://vegamovies.baby/?s=' + text




async def getmovie(url):
    response = requests.get(url)
    html = response.content.decode()
    soup = BeautifulSoup(html, "html.parser")
    link = soup.find_all("div", attrs={"class": "A2"})
    array = []
    print(url)
    for linnk in link:
        array.append(linnk.find("a").get("href"))
        if len(array) == 10:
            break
    result = array[:11]
    w = "https://filmy4wap.dev".join(result)
    g = "https://filmy4wap.dev" + w
    y = g.split(".html")
    
 
    #step : 2 - finding download link in Search result

    url2 = y[0]
    res = requests.get(url2)
    html2 = res.content.decode()
    soup2 = BeautifulSoup(html2,'html.parser')
    imglin = soup2.find_all("div",attrs={"class":"movie-thumb"})
    imig = []
    for imag in imglin:
        #print(imag.find('img').get('src'))
        imig.append(imag.find('img').get('src'))
        #print(imag.get('src'))
        break
    #print (imag.get('src'))
    global imgres
    imgres = imig
    #imgres = imgrs.replace(" ","%")
    #print(type(imgres))
    #print(imgres)
    str1 = ""
    for iimglink in imgres:
        str1 += iimglink
        break
    global fiinalimage2
    fiinalimage = str1.replace(" ","%")
    fiinalimage2 = fiinalimage
    print(fiinalimage2)

    for linkk in soup2.find_all('a',
        attrs={'href': re.compile("^/page-downloading-page/")}):
        break
    reallink = linkk.get('href')
    t =  "".join(reallink)
    k = "https://filmy4wap.dev" + t

    #print (k)
    #print ('\n')


    url3 = k
    res2 = requests.get(url3)
    html3 = res2.content.decode()
    soup3 = BeautifulSoup(html3,'html.parser')
    for linkk1 in soup3.find_all('a',
        attrs={'href': re.compile("^https://link2me.xyz/")}):
        break
    jaadu = linkk1.get('href')
    #print (jaadu)
    url4 = jaadu
    res3 = requests.get(url4)
    html4 = res3.content.decode()
    soup4 = BeautifulSoup(html4,'html.parser')
    super = soup4.find_all("div", attrs={"class": "dlink dl"})

    resse = []
    for linkk2 in super:
        resse.append(linkk2.find('a').get('href'))
        #finlink = linkk2.find('a').get('href')
    finlink = resse  
    #print (finlink)
    return "\n".join(finlink)

    
       

@bot.on_message(filters.command("start"))
def start(bot, message):
    bot.send_message(message.chat.id,"Welcome to MovieSearcher Bot\n Use this bot to search movies \n ex:- /Search moviename \nnote :- We didn't Allow piracy Bot use only Webscrapping algo. ")
@bot.on_message(filters.command(['search']))
async def sm(bot,message):
    await bot.send_message(message.chat.id,"Searching.... \n Bot By @IRoleEx \n Support US...")
    movie_name = " ".join(message.command[1:])
    url = 'https://filmy4wap.dev/site-1.html?to-search=' + movie_name
    resuult = await getmovie(url)
    await bot.send_message(message.chat.id,'Results of : '+ movie_name)
    #await bot.send_photo(message.chat.id, fiinalimage2)
    await bot.send_message(message.chat.id,resuult)
    await bot.send_message(message.chat.id,"bot by @iRoleEx")

if __name__ == "__main__":
    bot.run()
