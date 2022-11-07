import re
from dataclasses import replace
import time
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.client import Client
from pyrogram.types import InlineKeyboardButton as ikb
from pyrogram.types import InlineKeyboardMarkup as ikm

bot = Client("bot", bot_token="5744404637:AAFs-pq3UL34jqW1nti4eP8KOC8kf4Ncs_Q",
             api_id=1712043, api_hash="965c994b615e2644670ea106fd31daaf")

async def getmovie(url,url2):
    response = requests.get(url)
    html = response.content.decode()
    soup = BeautifulSoup(html, "html.parser")
    link = soup.find_all("div", attrs={"class": "A2"})
    array = []
    #print(url)
    try:
        for linnk in link:
            array.append(linnk.find("a").get("href"))
            if len(array) == 10:
                break
    except:
        pass
    ResPons = requests.get(url2)
    EchTiml = ResPons.content.decode()
    Soup11 = BeautifulSoup(EchTiml, "html.parser")
    ResultDekho = Soup11.find_all("div", attrs={"class": "title"})
    ResultArr = []
    for RealResult in ResultDekho:
        ResultArr.append(RealResult.find("a").get("href")) 
        break

    strarray = ""
    for realres in ResultArr:
        strarray = realres
        break
    print(strarray)

    global FinalResult
    FinalResult = strarray
    print (FinalResult)
    
    ResPonS7= requests.get(FinalResult)
    EchTimm7 = ResPonS7.content.decode()
    SoupPeelo = BeautifulSoup (EchTimm7,'html.parser')
    ResultDekho7 = SoupPeelo.find_all("div" ,attrs={"class":"wp-content"})
    picresult0 = SoupPeelo.find_all("div", attrs={"class": "poster"})

    Arr8 = []
    picarray = []
    for pic in picresult0:
            picarray.append(pic.find("img").get("src"))
            break
    strpic = ""
    for respic in picarray:
            strpic = respic
            break
        #print(strpic)
    
    global Finalpicture 
    Finalpicture = strpic
    for mainlink in ResultDekho7:
        Arr8.append(mainlink.find("a").get("href"))
        break
    
    #print(Arr8)
    Sipen = ""
    for sipen in Arr8:
        Sipen += sipen
        break
    print(Sipen)
    global FinalResultT
    FinalResultT = Sipen
    print (FinalResult)

   

    result = array[:11]
    w = "https://filmy4wap.dev".join(result)
    g = "https://filmy4wap.dev" + w
    y = g.split(".html")
    url2 = y[0]
    res = requests.get(url2)
    html2 = res.content.decode()
    soup2 = BeautifulSoup(html2, "html.parser")
    imglin = soup2.find_all("div", attrs={"class": "movie-thumb"})
    imig = []

    for imag in imglin:
        imig.append(imag.find("img").get("src"))
        break

    global imgres
    imgres = imig

    str1 = ""
    for iimglink in imgres:
        str1 += iimglink
        break

    global fiinalimage2
    fiinalimage = str1.replace(" ", "%20")
    fiinalimage2 = fiinalimage


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
    jaadu=None
    for linkk1 in soup3.find_all(
        "a", attrs={"href": re.compile("^https://link2me.xyz/")}
    ):
        jaadu = linkk1.get("href",None)
        break
    
    if jaadu == None:
        return "No link found"
    
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

async def getmovies (url3):
    response55 = requests.get(url3)
    html55 = response55.content.decode()
    soup55 = BeautifulSoup(html55, "html.parser")
    link55 = soup55.find_all("div", attrs={"class": "A2"})
    array55 = []

    for linki in link55:
        array55.append(linki.find("b").text)
        if len(array55) == 7:
            break

    global real_res
    real_res =  ""

    for relmin in array55:
        real_res += relmin + "\n\n"
        if len(real_res) == 7:
                break
    #print(real_res(-1))
        

        
    #print (real_res)
@bot.on_message(filters.command("start"))
def start(bot, message):
    bot.send_message(
        message.chat.id,
        "Welcome to MovieSearcher Bot\n Use this bot to search movies \n\n ex:- Type only Movie name in the bot \n Use /latest command for checking the latest list of movies\n\nnote :- We didn't Allow piracy \nBot use only Webscrapping algo. ",
    )
    #create a button for finlink using for loop


def my_buttons(finlink,xxlink,n):
    from pyrogram.types import InlineKeyboardButton as ikb
    from pyrogram.types import InlineKeyboardMarkup as ikm
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
    #print(ikm(NV1))
    return ikm(NV1)
def my_channel_id(data):
    async def get_my_member(_, c: Client, m: Message):
        #print(1)
        try:
            user_id=m.from_user.id
            #cmd = ['CREATOR','ADMINISTRATOR','MEMBER']
            get = await c.get_chat_member(data, user_id)
            status = get.status
            
            if status.ADMINISTRATOR or status.MEMBER or status.OWNER:
                print("true")
                return True
            else:
                await c.send_message(m. 
chat.id, "Join first https://t.me/+gs2qlZP-I1hiZmY1 \n Then can you Use the BOT")
                return False
        except Exception as e:
            print("error "+str(e))
            await c.send_message(m. 
chat.id, "Join first https://t.me/+gs2qlZP-I1hiZmY1 \n Then can you Use the BOT")
            return False
    return filters.create(get_my_member, data=data)


@bot.on_message(filters.text & my_channel_id(-1001859860307))
async def sm(bot, message):
    mess= await bot.send_message(message.chat.id, "searching....... \n Bot by - @IRoleEx")
    #button = ikb("Download", url=resse[1])

#await bot.send_message(message.chat.id, "Download", reply_markup=ikm([[button]]))
    movie_name = message.text
    url = "https://filmy4wap.dev/site-1.html?to-search=" + movie_name
    url2 = "https://hdmovie91.com/?s=" + movie_name
    kinbin=True
    await bot.send_message(message.chat.id,"Result are :- ",reply_markup=resuult)

    try:
        resuult = await getmovie(url,url2)
    
        await bot.send_photo(message.chat.id,Finalpicture,reply_markup=ikm([[ikb(text="Download", url=FinalResultT)]]))
        await bot.edit_message_text(message.chat.id,mess.id,"Search Completed 😊")
        time.sleep(2)
        await bot.delete_messages(message.chat.id,mess.id)
        kinbin=False
    except:
        pass
        
    try:
        await bot.send_photo(message.chat.id,fiinalimage2,caption="Result are :- ",reply_markup=resuult)
        await bot.edit_message_text(message.chat.id,mess.id,"Search Completed 😊")
        time.sleep(2)
        await bot.delete_messages(message.chat.id,mess.id)
        #await bot.send_message(message.chat.id,"Result are :- ",reply_markup=resuult)
        kinbin=False
    except:
        pass
    if kinbin:
        time.sleep(5)
        await bot.edit_message_text(mess.chat.id, mess.id,"Can not find **'"+message.text+"'** Movie in my Database \n\nBot by - @IRoleEx")
        time.sleep(3)
        await bot.delete_messages(message.chat.id, mess.id)
    
    #await bot.send_photo(message.chat.id, Finalpicture)

@bot.on_message(filters.command(["latest"]))
async def smp(bot, message):
    
    url3 = "https://filmy4wap.dev/site-1.html?to-search="
    resuult2 = await getmovies(url3)
    await bot.send_message(message.chat.id, "Here's are Some latest movies \n\n Bot by - @IRoleEx")
    await bot.send_message(message.chat.id, "Results of : " + "" + "Latest Movies" + "")
    await bot.send_message(message.chat.id, "Results are :- ",reply_markup=resuult2)
    await bot.send_message(message.chat.id, real_res)
    


if __name__ == "__main__":
    bot.run(print("bot started"))
