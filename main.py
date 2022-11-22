import requests
import re
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.client import Client
from pyrogram.types import InlineKeyboardButton as ikb
from pyrogram.types import InlineKeyboardMarkup as ikm
import time


#movie = input("Enter the movie name: ")
#url = "https://wwv11.watchmoviesonlinepk.com/search?s=" + movie

bot = Client(
    "bddot1",
    bot_token="5744404637:AAFE_x1pInEJWdLPWe1rOjql-of6R0cQsqs",
    api_id="1712043",
    api_hash="965c994b615e2644670ea106fd31daaf",
    #session_string="BQATJh3BDdT1EfhNHhoxrxy3ij44E5gfqJXusuFNGukp3IyFlE66jdnsPanR4W79_Jgrdwun5jDqJ76gSAPnXeCaOGL1TK-VEGLgf4HNgAOhdS3LZWCk251s8wgGf8wMD7Ft9tDUhT5w0Q95V5O_pLB1Fi3ic-MexDcAka-BJW8GuvonAMc0_hfFnICieo2Uj1hhOmO_XMIegfDC3NHBgdi9adX4pz4IF1t922fcvU7_R_5B4lol3LC3U9xbnrD3LoKF_qv5ujzhtdx6D8p0POFtSAK4KCIELh9stTfDpvGe9V6pJin-Xdq1a-uedTJ440YMIq9Bc9F9P1zKz9ORZ51jAAAAAT6V4FQA",
)

async def movieget(url,bot,message,mess):

    response = requests.get(url)
    html = response.content.decode()
    soup = BeautifulSoup(html, "html.parser")
    movies = soup.find_all("div", class_="boxtitle")
    link = []
    link2 = []
    for i in movies:
        link.append(i.find("a").get("href"))

        link2.append(i.find("a").get("title"))
        #print(link2)
        if len(link) == 3:
            break
        if len (link2) == 3:
            break
    #---------------------------------------------------------------------------------------------

    for j in link:  
        print ("\n") 
        response1 = requests.get(j)
        html1 = response1.content.decode()
        soup1 = BeautifulSoup(html1, "html.parser")
        moviename = soup1.find("div", attrs={"id": "entry_info"}).find("h1")
        mname = moviename.text #Movie Name Sequence Wise
        await bot.send_message(message.chat.id, "**"+ mname + "**")
        try:
            await bot.delete_messages(message.chat.id, mess.id)
        except:
            return ("No Movie Found")
        print (mname) 

    #---------------------------------------------------------------------------------------------

        movies1 = soup1.find("a", attrs={"href": re.compile("dood.to")})
        if movies1 is not None:
            s = movies1.get("href")
            x = "".join(s)
            y = "https:" + x
            print (y)
            await bot.send_message(message.chat.id,"Link-1 👇", reply_markup=ikm([[ikb("Download", url=y)]]))
        else:
            print ("Not Found Watchsb.com")

    #---------------------------------------------------------------------------------------------

        movies2 = soup1.find("a", attrs={"href": re.compile("akstream.xyz")})
        if movies2 is not None:
            s1 = movies2.get("href")
            x1 = "".join(s1)
            y1 = "https:" + x1
            print (y1)
            await bot.send_message(message.chat.id,"Link-2 👇",reply_markup=ikm([[ikb("Download", url=y1)]]))
        else:
            print ("Not found dood.to")

    #---------------------------------------------------------------------------------------------

        movies3 = soup1.find("a", attrs={"href": re.compile("streamtape.to")})
        if movies3 is not None:
            s2 = movies3.get("href")
            x2 = "".join(s2)
            y2 = "https:" + x2
            print (y2)
            await bot.send_message(message.chat.id,"Link-3 👇", reply_markup=ikm([[ikb("Download", url=y2)]]))
        else:
            print ("Not found akstream.xyz")

    #------------------------------------------------------------------------------------------ ---

    
@bot.on_message(filters.command('start'))
async def cos(bot,message):
    await bot.send_message(
        message.chat.id, "Welcome to MoVieSearcher Bot by iRoleEx"
    )
@bot.on_message(filters.text)
async def sm(bot, message):
    mess =await bot.send_message(
        message.chat.id, "**searching..**"
    )
    try:
        time.sleep(4)
        await bot.delete_messages(message.chat.id, mess.id)
    except:
        pass
    #h = await bot.send_photo(message.chat.id, "https://dl7.wapkizfile.info/download/aa706ef450726f5dc1d0c6076638abe7/7a099da6b7c00def02dad13bb823c39f/filmy4wap+wapkiz+com/Pathonpatham%20Noottandu%20(2022)%20South%20Hindi%20(HQ%20Dubbed)%20Full%20Movie%20HD.jpg")
    movie_name = message.text
    url = "https://wwv11.watchmoviesonlinepk.com/search?s=" + movie_name
    print ("Movie Url = ",url)
    await movieget(url, bot, message,mess)


bot.run(print("Bot On"))
