# -*- coding: utf-8 -*-
# Support <-> LeaBot-Version ===>##
import lea
from lea import *
from ley.ttypes import *
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
from time import sleep
import pyimgflip

#==============================================================================#

loop = asyncio.get_event_loop()
with open('tokenku.json', 'r') as bolo:
     pin = json.load(bolo)

#==============[ token 1 ]==============#
if pin['token'] == "":
    line = LINE()
else:
     try:
         line = LINE(pin['token'])
     except:
         pin['token'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         line = LINE()

pin['token'] = line.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 2 ]==============#
if pin['token2'] == "":
    ka = LINE()
else:
     try:
         ka = LINE(pin['token2'])
     except:
         pin['token2'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         ka = LINE()

pin['token2'] = ka.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 3 ]==============#
if pin['token3'] == "":
    kb = LINE()
else:
     try:
         kb = LINE(pin['token3'])
     except:
         pin['token3'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         kb = LINE()

pin['token3'] = kb.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#============[ token 4 ]=================#
if pin['token4'] == "":
    kc = LINE()
else:
     try:
         kc = LINE(pin['token4'])
     except:
         pin['token4'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         kc = LINE()

pin['token4'] = kc.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 5 ]==============#
if pin['token5'] == "":
    kd = LINE()
else:
     try:
         kd = LINE(pin['token5'])
     except:
         pin['token5'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         kd = LINE()

pin['token5'] = kd.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 6 ]==============#
if pin['token6'] == "":
    ke = LINE()
else:
     try:
         ke = LINE(pin['token6'])
     except:
         pin['token6'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         ke = LINE()

pin['token6'] = ke.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#============[ token 7 ]=================#
if pin['token7'] == "":
    k1 = LINE()
else:
     try:
         k1 = LINE(pin['token7'])
     except:
         pin['token7'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         k1 = LINE()

pin['token7'] = k1.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)
#==============[●●●●●●]==============#
print ("Login Succes")

cl = line
call = cl
oepoll = OEPoll(cl)
Bismillah=[cl,ka,kb,kc,kd]
Amin=[ka,kb,kc,kd]
Aakun=[kb,kc,kd,ke]
Bakun=[ka,kc,kd,ke]
Cakun=[ka,kb,kd,ke]
Dakun=[ka,kc,kb,ke]
Eakun=[ka,kb,kd,kc]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Smid = k1.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Smid]
Ley = ["uee6f3e2225d28c382c471a9cc648dc25"]
Lea = Bots+Ley
msg_dict = {}
msg_dict1 = {}
#==============[ Main Json ]==============#
main = codecs.open("Alfiah.json","r","utf-8")
Alfiah = json.load(main)
boters = codecs.open("Fia.json","r","utf-8")
Fia = json.load(boters)
zblacklist = codecs.open("Zie.json","r","utf-8")
Zie = json.load(zblacklist)

mulai = Alfiah

settings = {
    "gPicture":False,
    "cPicture":False,
    "likeStat":True,
    "LikeOn":True,
    "Jscancel":True,
    "like":4,
    "autoJoinTicket":False,
    "postingan":{},
    "Picture":False,
    "group":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

listTimeLiking = time.time()

def autolike():
   if settings['LikeOn'] == True:
     like = 1000+Alfiah['like']
     koment = Alfiah['comment']
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=like)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],koment+"\n\nBy: ✴☠$๓ţ☠✴\nhttp://line.me/ti/p/~semut0205")
            print ("Liked")
          except:
            pass
        else:
            print ("Already Liked")
   else:
    pass

def autoLike():
    listTimeLiking = time.time()
    if time.time() - listTimeLiking >= 60*60:
        listLikeType = [1001, 1002, 1003, 1004, 1005, 1006]
        myComment = "[Auto Like]"+\
                    "\nThis is AutoLike And Comment by: $๓ţ Self V.1"
        #feed = channel.getFeed()
        feed = cl.getFeed()
        if feed['message'] != 'success':
            listTimeLiking = time.time()
            return True
        del feed["result"]["feedInfos"]
        result = feed["result"]["feeds"]
        for res in result:
            postInfo = res["post"]["postInfo"]
            homeId = postInfo["homeId"]
            postId = postInfo["postId"]
            if settings["likeStat"] == True:
                continue
            else:
                #channel.likePost(homeId, postId, random.choice(listLikeType))
                client.likepost(homeId, postId, random.choice(listLikeType))
                #channel.createComment(homeId, postId, myComment)
                client.createComment(homeId, postId, myComment)
        listTimeLiking = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)


def cek(mid):
    if mid in (Bots):
        return True
    else:
        return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Sider Members ]═══════\n║ Sini Gabung Chat ka 😊..\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「reader {} member」\nhai ka.. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Alfiah["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「Member Join {}」\Wellcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Alfiah["welcome"]+"\ndi group : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Alfiah["keyCmd"]):
        cmd = pesan.replace(Alfiah["keyCmd"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Alfiah["keyCmd"]
    key = key.title()
    helpMessage = "═══════☣ℒℯα☣═══════╗\n║   「♛ɑɩҏɧɑԎ Լѻѵєяƽ♛」\n╠═══════☣ℒℯα☣═══════╝\n" + \
                  "║┍ℒℯα✍ ⚘ " + key + "Me\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Mid「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Info「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "kicker kick「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Kiss「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Bot kick「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Z1-5 kick「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Mybot\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Status\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "About\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "/reboot\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Runtime\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Creator\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Sp\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + ".sp\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "tag\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "woy\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "minggat\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "lea stay\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "lea join\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "lea bye.\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Leave「Namagrup」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Ginfo\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "ourl\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "zourl\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "curl\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "zcurl\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "all grup\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "zall urlgrup\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Gruplist\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "listbot\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Infogrup「angka」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Infomem「angka」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Myrechat\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Rechat\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Lurk「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Lurkers\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Sider「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Mepict\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Uppict\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Pictgrup\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Bcg:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Setkey「New Key」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Mykey\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Resetkey\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "ID line:「Id Line nya」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Sholat:「Nama Kota」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Cuaca:「Nama Kota」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Lokasi:「Nama Kota」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Music:「Judul Lagu」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Lirik:「Judul Lagu」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Yt3:「Judul Lagu」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Yt4:「Judul Video」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Profileig:「Nama IG」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "max:「angka」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Spamtag「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Scall:「jumlahnya」\n" + \
                  "║┕ℒℯα✍ ⚘ " + key + "Scall \n" + \
                  "╠═══════☣ℒℯα☣═══════╗\n║「™☠ᶩᵋᵅ ᵝᶱᶵ ѵєɍʂȋѻɳ☠™」\n╚═══════☣ℒℯα☣═══════╝"
    return helpMessage

def helpset():
    key = Alfiah["keyCmd"]
    key = key.title()
    helpMessage1 = "╔═══════☣ℒℯα☣═══════╗\n║   「♛ɑɩҏɧɑԎ Լѻѵєяƽ♛」\n╠═══════☣ℒℯα☣═══════╝\n" + \
                  "║┍ℒℯα✍ ⚘ " + key + "Notag「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Protect「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Proqr「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Projoin「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Autokick「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Procancel「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Sticker「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Respon「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Contact「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Autojoin「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Autoadd「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Welcome「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Autoleave「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Jticket「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Inta「on/off」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Bot:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Bot:dell\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "addbot「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "delbot「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Refresh\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "mybot\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "admin list\n" + \
                  "║┕ℒℯα✍ ⚘ " + key + "prolist\n" + \
                  "╠═══════☣ℒℯα☣═══════╗\n║「™☠ᶩᵋᵅ ᵝᶱᶵ ѵєɍʂȋѻɳ☠™」\n╚═══════☣ℒℯα☣═══════╝"
    return helpMessage1

def helpbot():
    key = Alfiah["keyCmd"]
    key = key.title()
    helpMessage2 = "═══════☣ℒℯα☣═══════╗\n║   「♛ɑɩҏɧɑԎ Լѻѵєяƽ♛」\n╠═══════☣ℒℯα☣═══════╝\n" + \
                  "║┍ℒℯα✍ ⚘ " + key + "Cban\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Ban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Unban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Ban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Unban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Tban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Utban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Tban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Utban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Banlist\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Tbanlist\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Refresh\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "cekmsg\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "sider:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "spam:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "add:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "tag:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "welcome:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "zname:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z1cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z2cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z3cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z4cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z5cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Kicker cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Kickerpict「K fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z1pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z2pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z3pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z4pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z5pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Gift:「Mid」「Jumlah」\n" + \
                  "║┕ℒℯα✍ ⚘ " + key + "Spam:「Mid」「Jumlah」\n" + \
                  "╠═══════☣ℒℯα☣═══════╗\n║「™☠ᶩᵋᵅ ᵝᶱᶵ ѵєɍʂȋѻɳ☠™」\n╚═══════☣ℒℯα☣═══════╝"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param1 in Zie["proqr"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        Zie["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                    X = random.choice(Bismillah).getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    Z = random.choice(Bismillah).getGroup(op.param1)
                    Z.preventedJoinByTicket = True
                    random.choice(Bismillah).updateGroup(Z)

        if op.type == 11:
            if op.param1 in Zie["pQr"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Zie["blacklist"] and op.param2 not in Lea:
                        Zie["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                    X = random.choice(Bismillah).getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    Z = random.choice(Bismillah).getGroup(op.param1)
                    Z.preventedJoinByTicket = True
                    random.choice(Bismillah).updateGroup(Z)

        if op.type == 11:
            if op.param2 in Zie["blacklist"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Lea and op.param2 not in Zie["Bots"] and op.param2 not in Zie["admin"]:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if ka.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Lea and op.param2 not in Zie["Bots"] and op.param2 not in Zie["admin"]:
                                ka.reissueGroupTicket(op.param1)
                                X = ka.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ka.updateGroup(X)
                                ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Lea and op.param2 not in Zie["Bots"] and op.param2 not in Zie["admin"]:
                                    kb.reissueGroupTicket(op.param1)
                                    X = kb.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kb.updateGroup(X)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Lea and op.param2 not in Zie["Bots"] and op.param2 not in Zie["admin"]:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Lea and op.param2 not in Zie["Bots"] and op.param2 not in Zie["admin"]:
                                            kd.reissueGroupTicket(op.param1)
                                            X = kd.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kd.updateGroup(X)
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Lea and op.param2 not in Zie["Bots"] and op.param2 not in Zie["admin"]:
                                                ke.reissueGroupTicket(op.param1)
                                                X = ke.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ke.updateGroup(X)
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 11:
            if op.param1 in Zie["intaPoint"]:
                if op.param2 in Lea and op.param2 in Zie["Bots"] and op.param2 not in Zie["admin"]:
                    pass
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == True:
                        pass
                    else:
                        cl.updateGroup(X)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)

        if op.type == 13:
            if op.param1 in Zie["pInvite"]:
               if op.param2 in Lea:
                  pass
               else:
                   if op.param2 not in Zie["blacklist"] and op.param2 not in Lea:
                      Zie["blacklist"][op.param2] = True
                      f=codecs.open('Znfblacklist.json','w','utf-8')
                      json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                   anu = random.choice(Bismillah).getCompactGroup(op.param1)
                   if anu.invitee is not None:
                         pipo = [a.mid for a in anu.invitee]
                         for target in pipo:
                             if target in op.param3:
                                random.choice(Bismillah).cancelGroupInvitation(op.param1,[target])
                                random.choice(Amin).kickoutFromGroup(op.param1,[target])
                         random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])          

        if op.type == 32:
           if op.param1 in Zie["pCancel"]:
              if op.param2 in Lea:
                 pass
              else:
                if op.param2 not in Zie["blacklist"] and op.param2 not in Lea:
                  Zie["blacklist"][op.param2] = True
                  f=codecs.open('Znfblacklist.json','w','utf-8')
                  json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                  try:
                    random.choice(Bismillah).getCompactGroup(op.param1)
                    random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                    random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Bismillah).acceptGroupInvitation(op.param1)
                  except:
                      pass

        if op.type == 32:
           if op.param2 in Zie["blacklist"]:
              if op.param2 in Lea:
                 pass
              else:
                 random.choice(Bismillah).getCompactGroup(op.param1)
                 random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                 random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                 random.choice(Bismillah).acceptGroupInvitation(op.param1)
                 random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 13:
            if mid in op.param3:
                if Alfiah["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        anu = cl.getContact(op.param2)
                        cl.sendMessageWithMention(op.param1,"maaf {} autoLeaveku on..send link aja " + str(anu.displayName))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Zie["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[_mid])
            if Amid in op.param3:
                if Alfiah["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        ka.acceptGroupInvitation(op.param1)
                        anu = ka.getContact(op.param2)
                        ka.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        group = ka.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Zie["blacklist"]:
                            ka.kickoutFromGroup(op.param1,[_mid])
            if Bmid in op.param3:
                if Alfiah["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        kb.acceptGroupInvitation(op.param1)
                        anu = kb.getContact(op.param2)
                        kb.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        group = kb.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Zie["blacklist"]:
                            kb.kickoutFromGroup(op.param1,[_mid])
            if Cmid in op.param3:
                if Alfiah["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        kc.acceptGroupInvitation(op.param1)
                        anu = kc.getContact(op.param2)
                        kc.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        group = kc.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Zie["blacklist"]:
                            kc.kickoutFromGroup(op.param1,[_mid])
            if Dmid in op.param3:
                if Alfiah["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        kd.acceptGroupInvitation(op.param1)
                        anu = kd.getContact(op.param2)
                        kd.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        group = kd.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Zie["blacklist"]:
                            kd.kickoutFromGroup(op.param1,[_mid])
            if Emid in op.param3:
                if Alfiah["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        ke.acceptGroupInvitation(op.param1)
                        anu = ke.getContact(op.param2)
                        ke.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        group = ke.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Zie["blacklist"]:
                            ke.kickoutFromGroup(op.param1,[_mid])

        if op.type == 13:
            if op.param1 in Zie["proInvite"]:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    try:
                        if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                            Zie["blacklist"][op.param2] = True
                            f=codecs.open('Znfblacklist.json','w','utf-8')
                            json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                            random.choice(Bismillah).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                                Zie["blacklist"][op.param2] = True
                                f=codecs.open('Znfblacklist.json','w','utf-8')
                                json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                group = cl.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                  if _mid not in Lea and _mid not in Fia["Bots"] and _mid not in Fia["admin"]:
                                    random.choice(Bismillah).cancelGroupInvitation(op.param1,[_mid])
                                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
            if op.param2 in Zie["blacklist"]:
               if op.param2 in Lea:
                  pass
               else:
                  try:
                      anu = random.choice(Bismillah).getCompactGroup(op.param1)
                      if anu.invitee is not None:
                            pipo = [a.mid for a in anu.invitee]
                            for target in pipo:
                                if target in op.param3:
                                    random.choice(Bismillah).cancelGroupInvitation(op.param1,[target])
                                    random.choice(Amin).kickoutFromGroup(op.param1,[target])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                  except:
                      pass
            if op.param3 in Zie["blacklist"]:
               if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                  pass
               else:
                    try:
                        if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                            Zie["blacklist"][op.param2] = True
                            f=codecs.open('Znfblacklist.json','w','utf-8')
                            json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                            random.choice(Bismillah).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 15:
            if op.param1 in Zie["leaveMsg"]:
                if op.param2 in Lea and op.param2 not in Fia["admin"] and op.param2 not in Fia["Bots"]:
                    return
                else:
                    cl.sendMessage(op.param1, Alfiah["leftmsg"])

        if op.type == 17:
            if op.param2 in Zie["blacklist"]:
                random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

            if op.param1 in Zie["welcome"]:
                if op.param2 in Lea or op.param2 in ["Bots"] or op.param2 in ["admin"]:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

            if op.param1 in Zie["proJoin"]:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                if op.param2 not in Zie["blacklist"]:
                    pass
                else:
                    try:
                        if op.param2 in Zie["blacklist"]:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param2 in Zie["blacklist"]:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param2 in Zie["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param2 in Zie["blacklist"]:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param2 in Zie["blacklist"]:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

        if op.type == 0:
            return

        if op.type == 5:
            if Alfiah["autoAdd"] == True:
                if op.param2 not in Lea:
                    if (Alfiah["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.findAndAddContactsByMid(op.param1)
                        cl.sendMessage(op.param1, Alfiah["message"])

        if op.type == 19:
            if op.param1 in Zie["proKick"]:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    if op.param2 not in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                        Zie["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        if op.param3 not in Zie["blacklist"]:
                            ke.findAndAddContactsByMid(op.param3)
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Zie["blacklist"]:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Zie["blacklist"]:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in Zie["blacklist"]:
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in Zie["blacklist"]:
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Lea:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.findAndAddContactsByMid(op.param3)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        x = k1.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        k1.leaveGroup(op.param1)
                        random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                    except:
                        random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                        random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Lea:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[mid])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[mid])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[mid])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kd.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kd.updateGroup(x)
                                    invsend = 0
                                    Ti = kd.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Amin).findAndAddContactsByMid(op.param3)
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Amid in op.param3:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        kb.findAndAddContactsByMid(op.param3)
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.findAndAddContactsByMid(op.param3)
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                ka.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ke.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ke.updateGroup(x)
                                    invsend = 0
                                    Ti = ke.reissueGroupTicket(op.param1)
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ka.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Aakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Aakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Aakun).inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Bmid in op.param3:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        kc.findAndAddContactsByMid(op.param3)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.findAndAddContactsByMid(op.param3)
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.findAndAddContactsByMid(op.param3)
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ka.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ka.updateGroup(x)
                                    invsend = 0
                                    Ti = ka.reissueGroupTicket(op.param1)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Bakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Bakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bakun).inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        kd.findAndAddContactsByMid(op.param3)
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.findAndAddContactsByMid(op.param3)
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Cakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Cakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Cakun).inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Dmid in op.param3:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        ke.findAndAddContactsByMid(op.param3)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kc.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kc.updateGroup(x)
                                    invsend = 0
                                    Ti = kc.reissueGroupTicket(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Dakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Dakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Dakun).inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Emid in op.param3:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kd.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kd.updateGroup(x)
                                    invsend = 0
                                    Ti = kd.reissueGroupTicket(op.param1)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Eakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Eakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Eakun).inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Smid in op.param3:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        ke.findAndAddContactsByMid(op.param3)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Amin).findAndAddContactsByMid(op.param3)
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return
            if op.param3 in Fia["Bots"]:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                                            random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return
            if op.param3 in Fia["admin"]:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    Zie["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                                            random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return

        if op.type == 32:
            if op.param1 in Zie["proCancel"]:
                if op.param2 in Lea and op.param2 in Fia["Bots"] and op.param2 in Fia["admin"]:
                    pass
                else:
                    if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                        Zie["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                        user = cl.getContact(op.param2)
                        random.choice(Amin).sendMessage(op.param1,"In protection ,, you not admin!! " + str(user.displayName))
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        try:
                            if op.param3 in Lea:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 in Fia["Bots"]:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 in Fia["admin"]:
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param3 not in Fia["blacklist"]:
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        pass

            if Smid in op.param3:
                if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                    Zie["blacklist"][op.param2] = True
                    f=codecs.open('Znfblacklist.json','w','utf-8')
                    json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[Smid])
            if op.param3 in Lea:
                if op.param2 not in Lea and op.param2 not in Fia["Bots"] and op.param2 not in Fia["admin"]:
                    Zie["blacklist"][op.param2] = True
                    f=codecs.open('Znfblacklist.json','w','utf-8')
                    json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Amin).findAndAddContactsByMid(op.param3)
                    random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 55:
            try:
                if op.param1 in Alfiah["readPoint"]:
                   if op.param2 in Alfiah["readMember"][op.param1]:
                       pass
                   else:
                       Alfiah["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

            if op.param2 in Zie["blacklist"]:
                if op.param2 not in Lea and op.param2 not in Fia["admin"] and op.param2 not in Fia["Bots"]:
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 65:
            if Alfiah["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if Alfiah["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if "MENTION" in msg.contentMetadata.keys() != None:
                  if Alfiah['detectMention'] == True:
                      contact = cl.getContact(msg._from)
                      cName = contact.pictureStatus
                      balas = ["http://dl.profile.line-cdn.net/" + cName]
                      ret_ = random.choice(balas)
                      mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                      mentionees = mention["MENTIONEES"]
                      for mention in mentionees:
                            if mention["M"] in mid:
                                   cl.sendMessage(msg.to, Alfiah["msgTag"])
                                   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13002263","STKPKGID":"1322343","STKVER":"1"}, contentType=7)
                                   break
                if 'MENTION' in msg.contentMetadata.keys() != None:
                  if Alfiah["Mentionkick"] == True:
                      contact = cl.getContact(msg._from)
                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                      mentionees = mention['MENTIONEES']
                      for mention in mentionees:
                            if mention['M'] in mid:
                                   cl.mentiontag(msg.to,[msg._from])
                                   cl.sendMessage(msg.to,"don't tag me...")
                                   cl.kickoutFromGroup(msg.to,[msg._from])
                                   break

            if msg.contentType == 7:
              if Alfiah["sticker"] == True:
                  msg.contentType = 0
                  cl.sendMessage(msg.to,"•「Check ID Sticker」•\n STKID : " + msg.contentMetadata["STKID"] + "\n STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])

            if msg.contentType == 13:
              if Alfiah["contact"] == True:
                 msg.contentType = 0
                 cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                 if 'displayName' in msg.contentMetadata:
                     contact = cl.getContact(msg.contentMetadata["mid"])
                     path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                     image = 'http://dl.profile.line.naver.jp'+path
                     cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                     cl.sendImageWithURL(msg.to, image)
            if msg.contentType == 16:
              if settings['LikeOn'] == True:
                  try:
                      typel = [1001,1002,1003,1004,1005,1006]
                      url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                      st = url['result']["homeId"]
                      for i in range(len(st)):
                          test = st[i]
                          result = test['posts']['postInfo']['postId']
                          cl.like(str(st), str(result), likeType=random.choice(typel))
                          cl.comment(str(st), str(result), 'Manual like by: $๓ţ')
                  except:
                      pass
            if msg.contentType == 16:
              if Alfiah["checkPost"] == True:
                  try:
                      ret_ = "╔════[ Post Detail ]"
                      if msg.contentMetadata["serviceType"] == "GB":
                          contact = cl.getContact(sender)
                          auth = "\n╠☛ Author : {}".format(str(contact.displayName))
                      else:
                          auth = "\n╠☛ Author : {}".format(str(msg.contentMetadata["serviceName"]))
                      purl = "\n╠☛ Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                      ret_ += auth
                      ret_ += purl
                      if "mediaOid" in msg.contentMetadata:
                          object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                          if msg.contentMetadata["mediaType"] == "V":
                              if msg.contentMetadata["serviceType"] == "GB":
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                  murl = "\n╠☛ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                              else:
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                  murl = "\n╠☛ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                              ret_ += murl
                          else:
                              if msg.contentMetadata["serviceType"] == "GB":
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                              else:
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                          ret_ += ourl
                      if "stickerId" in msg.contentMetadata:
                          stck = "\n╠☛ Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                          ret_ += stck
                      if "text" in msg.contentMetadata:
                          text = "\n╠☛ Note : {}".format(str(msg.contentMetadata["text"]))
                          ret_ += text
                      ret_ += "\n╚══[ $๓ţ SELF V.1 ]"
                      cl.sendMessage(to, str(ret_))
                  except:
                      cl.sendMessage(msg.to,"Invalid Post")

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if Alfiah["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"╔══════════════\n╠☛❲Check Sticker❳\n╠☛ STKID : " + msg.contentMetadata["STKID"] +"\n╠☛ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n╠☛ STKVER : " + msg.contentMetadata["STKVER"] + "\n╠☛ " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\n╚══════════════")
               if msg.contentType == 13:
                 if Alfiah["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╔══════════════\n╠☛ Nama : " + msg.contentMetadata["displayName"] + "\n╠☛ Mid : " + msg.contentMetadata["mid"] + "\n╠☛ Status : " + contact.statusMessage + "\n╠☛ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n╚══════════════")
                        cl.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                 if msg._from in Ley:
                  if Alfiah["abots"] == True:
                    if msg.contentMetadata["mid"] in Fia["Bots"]:
                        cl.sendMessage(msg.to,"was bot friend")
                    else:
                        Fia["Bots"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add bots")
                 if Alfiah["dbots"] == True:
                    if msg.contentMetadata["mid"] in Fia["Bots"]:
                        del Fia["Bots"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove bots")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list bots")

                 if msg._from in Ley:
                  if Alfiah["addadmin"] == True:
                    if msg.contentMetadata["mid"] in Fia["admin"]:
                        cl.sendMessage(msg.to,"was admin")
                    else:
                        Fia["admin"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add admin")
                 if Alfiah["deladmin"] == True:
                    if msg.contentMetadata["mid"] in Fia["admin"]:
                        del Fia["admin"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove admin")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list admin")

                 if msg._from in Ley:
                  if Alfiah["ablacklist"] == True:
                    if msg.contentMetadata["mid"] in Zie["blacklist"]:
                        cl.sendMessage(msg.to,"was blacklist")
                    else:
                        Zie["blacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add in blacklist")
                 if Alfiah["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in Zie["blacklist"]:
                        del Zie["blacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove blacklist")
                    else:
                        cl.sendMessage(msg.to,"Contact not in blacklist")

                 if msg._from in Ley:
                  if Alfiah["Tablacklist"] == True:
                    if msg.contentMetadata["mid"] in Zie["Talkblacklist"]:
                        cl.sendMessage(msg.to,"was Talkblacklist")
                    else:
                        Zie["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add in Talkblacklist")
                 if Alfiah["Tdblacklist"] == True:
                    if msg.contentMetadata["mid"] in Zie["Talkblacklist"]:
                        del Zie["Talkblacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove Talkblacklist")
                    else:
                        cl.sendMessage(msg.to,"Contact not in Talkblacklist")

               if msg.contentType == 1:
                 if msg._from in Ley:
                    if Alfiah["Aimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Alfiah["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succses")
                        Alfiah["Img"] = {}
                        Alfiah["Aimage"] = False

               if msg.toType == 2:
                 if msg._from in Ley:
                   if settings["gPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["gPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes")

               if msg.contentType == 1:
                   if msg._from in Ley:
                       if mid in Alfiah["foto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Alfiah["foto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Succes")

               if msg.contentType == 1:
                 if msg._from in Ley:
                        if Amid in Alfiah["foto"]:
                            path = ka.downloadObjectMsg(msg_id)
                            del Alfiah["foto"][Amid]
                            ka.updateProfilePicture(path)
                            ka.sendMessage(msg.to,"Succes")
                        elif Bmid in Alfiah["foto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Alfiah["foto"][Bmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Succes")
                        elif Cmid in Alfiah["foto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Alfiah["foto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Succes")

               if msg.contentType == 1:
                 if msg._from in Ley:
                   if settings["cPicture"] == True:
                     path1 = ka.downloadObjectMsg(msg_id)
                     path2 = kb.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["cPicture"] = False
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "Succes change pic")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Succes change pic")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Succes change pic")

               if msg.contentType == 0:
                    if Alfiah["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "menu":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               helpMessage = help()
                               cl.sendMessage(to,"╔"+str(helpMessage))

                        if cmd == "menubot":
                            if msg._from in Ley:
                               helpMessage = help()
                               ka.sendMessage(to,"╔"+str(helpMessage))

                        if cmd == "menu1":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               helpMessage1 = helpset()
                               cl.sendMessage(to,str(helpMessage1))

                        if cmd == "menubot1":
                            if msg._from in Ley:
                               helpMessage1 = helpset()
                               ka.sendMessage(to,"╔"+str(helpMessage1))

                        if cmd == "on":
                            if msg._from in Ley:
                                Alfiah["selfbot"] = True
                                cl.sendMessage(msg.to, "Bot mu sudah diaktifkan")

                        elif cmd == "off":
                            if msg._from in Ley:
                                Alfiah["selfbot"] = False
                                cl.sendMessage(msg.to, "Bot mu telah di matikan")

                        if cmd == "tbanon":
                            if msg._from in Ley:
                                Alfiah["talkban"] = True
                                cl.sendMessage(msg.to, "kick Talkban on")

                        elif cmd == "tbanoff":
                            if msg._from in Ley:
                                Alfiah["talkban"] = False
                                cl.sendMessage(msg.to, "kick Talkban off")

                        elif cmd == "menu2":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               helpMessage2 = helpbot()
                               cl.sendMessage(to,"╔"+str(helpMessage2))

                        elif cmd == "menubot2":
                            if msg._from in Ley:
                               helpMessage2 = helpbot()
                               ka.sendMessage(to,"╔"+str(helpMessage2))

                        elif cmd == "grupset":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                md = ""
                                if msg.to in Zie["proqr"]: md+="􁤁􀇜╠☛ PʀᴏQr : ✓\n"
                                else: md+="􀔃􀆓╠☛ PʀᴏQr: ✘\n"
                                if msg.to in Zie["proJoin"]: md+="􁤁􀇜╠☛ PʀᴏJᴏɪɴ : ✓\n"
                                else: md+="􀔃􀆓╠☛ PʀᴏJᴏɪn : ✘\n"
                                if msg.to in Zie["proKick"]: md+="􁤁􀇜╠☛ Auto ᴋɪᴄᴋ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Auto ᴋɪᴄᴋ : ✘\n"
                                if msg.to in Zie["proCancel"]: md+="􁤁􀇜╠☛ Pʀᴏᴄᴀɴᴄᴇʟ : ✓\n"
                                else: md+="􀔃􀆓╠☛ PʀᴏᴄᴀɴᴄᴇL : ✘\n"
                                if msg.to in Zie["intaPoint"]: md+="􁤁􀇜╠☛ IntaPoint : ✓\n"
                                else: md+="􀔃􀆓╠☛ IntaPoint : ✘\n"
                                if msg.to in Zie["Talkblacklist"]: md+="􁤁􀇜╠☛ ReadKick : ✓\n"
                                else: md+="􀔃􀆓╠☛ ReadKick : ✘\n"
                                if msg.to in Zie["welcome"]: md+="􁤁􀇜╠☛ welcome : ✓\n"
                                else: md+="􀔃􀆓╠☛ Welcome : ✘\n"
                                if msg.to in Zie["leaveMsg"]: md+="􁤁􀇜╠☛ Leave Msg : ✓\n"
                                else: md+="􀔃╠☛ Leave Msg : ✘\n"
                                #userid = "https://line.me/ti/p/~" + cl.profile.userid
                                #cl.sendFooter(to,"╔═══❲ Sett Group ❳════\n"+ md +"╚══════════════", userid, "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName)
                                cl.sendMessage(msg.to, "╔═══❲ Sett Group ❳════\n"+ md +"╚══════════════")

                        elif text.lower() == "status":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                md = ""
                                if Alfiah["autoJoin"] == True: md+="􁤁􀇜╠☛ AᴜᴛᴏJᴏɪɴ : ✓\n"
                                else: md+="􀔃􀆓╠☛ AutoJoin : ✘\n"
                                if Alfiah["sticker"] == True: md+="􁤁􀇜╠☛ Stickeʀ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Stickeʀ ✘\n"
                                if Alfiah["contact"] == True: md+="􁤁􀇜╠☛ Cᴏntacᴛ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Cᴏntacᴛ : ✘ \n"
                                if Alfiah["Mentionkick"] == True: md+="􁤁􀇜╠☛ AutoKick Mention : ✓\n"
                                else: md+="􀔃􀆓╠☛ AutoKick Mention : ✘\n"
                                if Alfiah["detectMention"] == True: md+="􁤁􀇜╠☛ Mention : ✓\n"
                                else: md+="􀔃􀆓╠☛ Mention : ✘\n"
                                if Alfiah["autoAdd"] == True: md+="􁤁􀇜╠☛ Msg ᴀᴅᴅ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Msg ᴀᴅᴅ : ✘\n"
                                if Alfiah["autoLeave"] == True: md+="􁤁􀇜╠☛ Auto Lᴇᴀᴠᴇ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Auto Lᴇᴀᴠᴇ : ✘\n"
                                #userid = "https://line.me/ti/p/~" + cl.profile.userid
                                #cl.sendFooter(to,"╔═══❲ Status Group ❳════\n"+ md +"╚══════════════", userid, "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName)
                                cl.sendMessage(msg.to, "╔═══❲ Status Group ❳════\n"+ md +"╚══════════════")

                        elif cmd == "me" or text.lower() == 'me':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               cl.sendMentionFooter(to, '「My Name」\n', sender, "https://line.me/ti/p/Qs-GbY_YPG", "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName);cl.sendMessage(to, cl.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+cl.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/semut0205', 'type': 'mt', 'subText': "✴☠$๓ţ { $€๓µţ ๓€яąЂ ţ€ą๓ }☠✴", 'a-installUrl': 'https://line.me/ti/p/~calon_almarhum99', 'a-installUrl': ' https://line.me/ti/p/semut0205', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/semut0205', 'i-linkUri': 'https://line.me/ti/p/semut0205', 'id': 'mt000000000a6b79f9', 'text': '✴☠$๓ţ { $€๓µţ ๓€яąЂ ţ€ą๓ }☠✴', 'linkUri': 'https://line.me/ti/p/semut0205'}, contentType=19)

                        elif ("Gn " in msg.text):
                          if msg._from in Ley:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gn ","")
                              cl.updateGroup(X)

                        elif 'Like ' in text.lower():
                          if msg._from in Ley:
                              try:
                                  typel = [1001,1002,1003,1004,1005,1006]
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  a = cl.getContact(u).mid
                                  s = cl.getContact(u).displayName
                                  hasil = cl.getHomeProfile(mid=a)
                                  st = hasil['result']["homeId"]
                                  for i in range(len(st)):
                                      test = st[i]
                                      result = test['posts']['postInfo']['postId']
                                      cl.like(str(sender), str(result), likeType=random.choice(typel))
                                      cl.comment(str(sender), str(result), 'AUTO_Like by: $๓ţ Bot SELF_V.1')
                                  cl.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                              except Exception as e:
                                  cl.sendMessage(receiver, str(e))

                        elif cmd == " like all" or text.lower() == 'like':
                                hasil = cl.getHome(msg._from)
                                zxc =  hasil['result']['homeInfo']['postCount']
                                for zx in range(0,zxc):
                                  if hasil['result']['feeds'][zx]['post']['postInfo']['liked'] == False:
                                    try:
                                      cl.like(hasil['result']['feeds'][zx]['post']['userInfo']['mid'],hasil['result']['feeds'][zx]['post']['postInfo']['postId'],likeType=1000+Alfiah['like'])
                                      cl.comment(hasil['result']['feeds'][zx]['post']['userInfo']['mid'],hasil['result']['feeds'][zx]['post']['postInfo']['postId'],Alfiah['comment']+"\n\nAutoLike by: ✴☠$๓ţ☠✴\nhttp://line.me/ti/p/~semut0205")
                                    except:
                                       pass
                                  else:
                                     pass
                                cl.sendMessage(msg.to,"Done") 

                        elif ("Mid " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               if 'MENTION' in msg.contentMetadata.keys()!= None:
                                   names = re.findall(r'@(\w+)', text)
                                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   mentionees = mention['MENTIONEES']
                                   lists = []
                                   for mention in mentionees:
                                       if mention["M"] not in lists:
                                           lists.append(mention["M"])
                                   ret_ = ""
                                   for ls in lists:
                                       ret_ += "{}".format(str(ls))
                                   cl.sendMessage(to, str(ret_),{'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+'M', 'AGENT_NAME': 'Mention', 'AGENT_LINK': 'http://line.me/ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath})

                        elif ("Info " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               ka.sendContact(msg.to, Amid)
                               time.sleep(0.15)
                               kb.sendContact(msg.to, Bmid)
                               time.sleep(0.15)
                               kc.sendContact(msg.to, Cmid)
                               time.sleep(0.15)
                               kd.sendContact(msg.to, Dmid)
                               time.sleep(0.15)
                               ke.sendContact(msg.to, Emid)

                        elif text.lower() == "myrechat":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "rechat":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               try:
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                               except:
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")
                                   k1.removeAllMessages(op.param2)
                                   k1.sendMessage(msg.to,"ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ membersihkan ")

                        elif cmd.startswith("bcg: "):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               cl.sendMessage(msg.to, "key Now「 " + str(Alfiah["keyCmd"]) + " 」")

                        elif cmd.startswith("setkey "):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "change key failed")
                               else:
                                   Alfiah["keyCmd"] = str(key).lower()
                                   cl.sendMessage(msg.to, "succes at「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               Alfiah["keyCmd"]=""
                               cl.sendMessage(msg.to, "succes resset key command")

                        elif cmd == "/reboot":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               cl.sendMessage(msg.to, "waiting a second")
                               Alfiah["rePoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "bot was restarting")

                        elif cmd == "runtime":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               eltime = time.time() - listTimeLiking
                               bot = "was run " +waktu(eltime)
                               cl.sendMessage(to, bot,)

                        elif cmd == "ginfo":
                          if msg._from in Ley:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup"):
                          if msg._from in Ley:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "No file"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "  •⌻ List Grup Info ⌻•\n"
                                ret_ += "\n⌬ Nama Group : {}".format(G.name)
                                ret_ += "\n⌬ ID Group : {}".format(G.id)
                                ret_ += "\n⌬ Pembuat : {}".format(gCreator)
                                ret_ += "\n⌬ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n⌬ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n⌬ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n⌬ Group Qr : {}".format(gQr)
                                ret_ += "\n⌬ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "● "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"● Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except:
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ka.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    ka.sendMessage(msg.to,"Succes leave in group " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z1grup":
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = ka.getGroupIdsJoined()
                               for i in gid:
                                   G = ka.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ka.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z2grup":
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z3grup":
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z4grup":
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = kd.getGroupIdsJoined()
                               for i in gid:
                                   G = kd.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kd.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z5grup":
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "kickergrup":
                            if msg._from in Ley:
                               ma = ""
                               a = 0
                               gid = k1.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "ourl":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "curl":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "done°")

                        elif cmd == "zourl":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                if msg.toType == 2:
                                   X = ka.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ka.updateGroup(X)
                                gurl = ka.reissueGroupTicket(msg.to)
                                ka.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "zcurl":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                if msg.toType == 2:
                                   X = ka.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ka.updateGroup(X)
                                   ka.sendMessage(msg.to, "done°")

                        elif cmd == "all urlgrup":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "●Nama : "+str(x.name)+ "\n● Url grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "zall urlgrup":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                if msg.toType == 2:
                                   x = ka.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ka.updateGroup(x)
                                   gurl = ka.reissueGroupTicket(msg.to)
                                   ka.sendMessage(msg.to, "● Nama : "+str(x.name)+ "\n● Url grup : http://line.me/R/ti/g/"+gurl)

#===========================================#
                        elif cmd == "pictgrup":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              if msg.toType == 2:
                                settings["gPicture"] = True
                                cl.sendMessage(msg.to,"please send pict")

                        elif cmd == "mepict":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                settings["cPicture"] = True
                                cl.sendMessage(msg.to,"please send pict")

                        elif cmd == "uppict":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["foto"][mid] = True
                                cl.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z1pict":
                            if msg._from in Ley:
                                Alfiah["foto"][Amid] = True
                                ka.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z2pict":
                            if msg._from in Ley:
                                Alfiah["foto"][Bmid] = True
                                kb.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z3pict":
                            if msg._from in Ley:
                                Alfiah["foto"][Cmid] = True
                                kc.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z4pict":
                            if msg._from in Ley:
                                Alfiah["foto"][Dmid] = True
                                kd.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z5pict":
                            if msg._from in Ley:
                                Alfiah["foto"][Emid] = True
                                ke.sendMessage(msg.to,"please Send pict")

                        elif cmd == "kickerpict":
                            if msg._from in Ley:
                                Alfiah["foto"][Smid] = True
                                k1.sendMessage(msg.to,"please Send pict")

                        elif cmd.startswith("zname: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z1cn: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z2cn: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z3cn: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z4cn: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z5cn: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("kicker cn: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd == "sepi" or text.lower() == 'mention':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "bot":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"  ✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴ Botz\n\n"+ma+"\nTotal : %sBot" %(str(len(Bots))))

                        elif cmd == "adminlist":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                mb = ""
                                b = 0
                                for m_id in Fia["admin"]:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"ADMIN: "+mb+"\nTotal :「✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴」\n Admin Bot" %(str(len(admin))))

                        elif cmd == "respon":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                ka.sendMessage(msg.to,"✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                kb.sendMessage(msg.to,"✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                kc.sendMessage(msg.to,"✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                kd.sendMessage(msg.to,"✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                ke.sendMessage(msg.to,"✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")

                        elif text.lower() == "response":
                            if msg._from in Ley:
                                if msg.to in Zie["proCancel"] or msg.to in Zie["proInvite"]:
                                    cl.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                else:
                                    Zie["pCancel"][msg.to] = True
                                    Zie["pInvite"][msg.to] = True
                                    Zie["pQr"][msg.to] = True
                                    f=codecs.open('Znfblacklist.json','w','utf-8')
                                    json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ka.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    kb.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    kc.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    kd.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    ke.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")

                        elif cmd == ".inv":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                try:
                                    ang = [Amid,Bmid,Cmid,Dmid,Emid]
                                    cl.inviteIntoGroup(msg.to, ang)
                                    ka.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "js stay":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                try:
                                    ang = [Smid]
                                    cl.inviteIntoGroup(msg.to, ang)
                                except:
                                    ka.inviteIntoGroup(msg.to, ang)

                        elif cmd == "js bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = k1.getGroup(msg.to)
                                k1.sendMessage(msg.to, "see u member "+str(G.name))
                                k1.leaveGroup(msg.to)

                        elif cmd == "z1bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = ka.getGroup(msg.to)
                                ka.sendMessage(msg.to, "see u member "+str(G.name))
                                ka.leaveGroup(msg.to)

                        elif cmd == "z2bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = kb.getGroup(msg.to)
                                kb.sendMessage(msg.to, "see u member "+str(G.name))
                                kb.leaveGroup(msg.to)

                        elif cmd == "z3bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = kc.getGroup(msg.to)
                                kc.sendMessage(msg.to, "see u member "+str(G.name))
                                kc.leaveGroup(msg.to)

                        elif cmd == "z4bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = kd.getGroup(msg.to)
                                kd.sendMessage(msg.to, "see u member "+str(G.name))
                                kd.leaveGroup(msg.to)

                        elif cmd == "z5bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = ke.getGroup(msg.to)
                                ke.sendMessage(msg.to, "see u member "+str(G.name))
                                ke.leaveGroup(msg.to)

                        elif cmd == "all":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "byeall":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ka.sendMessage(msg.to, "Bye,,,bye... 😎 "+str(G.name))
                                kb.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                ka.leaveGroup(msg.to)

                        elif cmd == "/bye":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "see u member "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in Ley:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ka.sendMessage(i, "")
                                        kb.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        ka.sendMessage(to,"Leave succes from " +h)

                        elif cmd == "z1join":
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)

                        elif cmd == "z2join":
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "z3join":
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "z4join":
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "z5join":
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "js join":
                            if msg._from in Ley:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)

                        elif cmd == ".speed respon":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "🚩response 🚩\n\n - 🌏 Speed Profile\n   %.10f\n - ➡ Speed Contact\n   %.10f\n - ➡ Speed Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               start = time.time()
                               cl.sendMessage(to, "•••")
                               elapsed_time = time.time() - start
                               cl.sendMessage(to,format(str(elapsed_time)))

                        elif cmd == ".speed" or cmd == ".sp":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               start = time.time()
                               ka.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start
                               ka.sendMessage(msg.to, "%s s" % (elapsed_time))

                               start2 = time.time()
                               kb.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start2
                               kb.sendMessage(msg.to, "%s s" % (elapsed_time))

                               start3 = time.time()
                               kc.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start3
                               kc.sendMessage(msg.to, "%s " % (elapsed_time))

                               start4 = time.time()
                               kd.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start4
                               kd.sendMessage(msg.to, "%s s" % (elapsed_time))

                               start5 = time.time()
                               ke.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start5
                               ke.sendMessage(msg.to, "%s s" % (elapsed_time))

                        elif cmd == "lurk on":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Alfiah['readPoint'][msg.to] = msg_id
                                 Alfiah['readMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurk off":
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Alfiah['readPoint'][msg.to]
                                 del Alfiah['readMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurkers":
                          if msg._from in Ley:
                            if msg.to in Alfiah['readPoint']:
                                if Alfiah['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Alfiah['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n⌬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Alfiah['readPoint'][msg.to]
                                        del Alfiah['readMember'][msg.to]
                                    except:
                                        pass
                                    Alfiah['readPoint'][msg.to] = msg.id
                                    Alfiah['readMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on ")

                        elif cmd == "sider on":
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "╔══════════════\n╠☛ starting cek sider\n╚══════════════\n╔══════════════\n╠☛ date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠☛ hour "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "╔══════════════\n╠☛ sider off mode\n╚══════════════")
                              else:
                                  cl.sendMessage(msg.to, "sider in off mode")

                        elif cmd.startswith("sholat: "):
                          if msg._from in Ley:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n Lokasi : " + data[0]
                                         ret_ += "\n⌬ " + data[1]
                                         ret_ += "\n⌬ " + data[2]
                                         ret_ += "\n⌬ " + data[3]
                                         ret_ += "\n⌬ " + data[4]
                                         ret_ += "\n⌬ " + data[5]
                                         ret_ += "\n\n Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\n Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in Ley:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in Ley:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n Location : " + data[0]
                                    ret_ += "\n Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in Ley:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik tidak ditemukan")

                        elif cmd.startswith("music: "):
                           if msg._from in Ley:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "Loading....")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "Musik tidak ditemukan")

                        elif cmd.startswith("zimage: "):
                          if msg._from in Ley:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("yt4: "):
                          if msg._from in Ley:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("yt3: "):
                          if msg._from in Ley:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in Ley:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = " Link : " + "https://www.instagram.com/" + instagram
                                text = " Name : "+namaIG+"\n Username : "+usernameIG+"\n Biography : "+bioIG+"\n Follower : "+followerIG+"\n Following : "+followIG+"\n Post : "+mediaIG+"\n Verified : "+verifIG+"\n Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in Ley:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"⇸「 I N F O 」⇷\n\n"+" Date Of Birth : "+lahir+"\n Age : "+usia+"\n Ultah : "+ultah+"\n Zodiak : "+zodiak)

                        elif cmd.startswith("max: "):
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Alfiah["Maxlimit"] = num
                                cl.sendMessage(msg.to,"Max spam Tag " +strnum)

                        elif cmd.startswith("scall: "):
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Alfiah["limit"] = num
                                cl.sendMessage(msg.to,"Max spam call " +strnum)

                        elif cmd.startswith("stag "):
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Alfiah["Maxlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")

                        elif cmd == "scall":
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Alfiah["limit"])
                                cl.sendMessage(to, "Succes {} Spam Call".format(str(Znfwait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                         cl.acquireGroupCallRoute(to)
                                         cl.inviteIntoGroupCall(to, contactIds=members)
                                     except:
                                         pass
                                else:
                                    cl.sendMessage(to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Alfiah["spamMsg"]))
                                      ka.sendMessage(midd, str(Alfiah["spamMsg"]))
                                      kb.sendMessage(midd, str(Alfiah["spamMsg"]))
                                      kc.sendMessage(midd, str(Alfiah["spamMsg"]))
                                      kd.sendMessage(midd, str(Alfiah["spamMsg"]))
                                      ke.sendMessage(midd, str(Alfiah["spamMsg"]))

                        elif 'ID line: ' in msg.text:
                          if Alfiah["selfbot"] == True:
                           if msg._from in Ley:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif 'Welcome ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in Zie["welcome"]:
                                       msgs = "Msg Welcome was on"
                                  else:
                                       Zie["welcome"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["welcome"]:
                                         del Zie["welcome"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Msg welcome mode on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Left ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Left ','')
                              if spl == 'on':
                                  if msg.to in Zie["leaveMsg"]:
                                       msgs = "Msg Left was on"
                                  else:
                                       Zie["leaveMsg"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["leaveMsg"]:
                                         del Zie["leaveMsg"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Msg Leave mode on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Proqr ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in Zie["proqr"]:
                                       msgs = "Succes"
                                  else:
                                       Zie["proqr"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["proqr"]:
                                         del Zie["proqr"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Autokick ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Autokick ','')
                              if spl == 'on':
                                  if msg.to in Zie["proKick"]:
                                       msgs = "Autokick on"
                                  else:
                                       Zie["proKick"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["proKick"]:
                                         del Zie["proKick"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Autokick off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Projoin ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in Zie["proJoin"]:
                                       msgs = "Projoin on"
                                  else:
                                       Zie["proJoin"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["proJoin"]:
                                         del Zie["proJoin"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Projoin off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in Zie["proCancel"]:
                                       msgs = "Procancel on"
                                  else:
                                       Zie["proCancel"] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["proCancel"]:
                                         Zie["proCancel"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Procancel off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in Zie["proqr"]:
                                       msgs = ""
                                  else:
                                       Zie["proqr"][msg.to] = True
                                  if msg.to in Zie["proKick"]:
                                      msgs = ""
                                  else:
                                       Zie["proKick"][msg.to] = True
                                  if msg.to in Zie["proInvite"]:
                                      msgs = ""
                                  else:
                                       Zie["proInvite"][msg.to] = True
                                  if msg.to in Zie["proJoin"]:
                                      msgs = ""
                                  else:
                                       Zie["proJoin"][msg.to] = True
                                  if msg.to in Zie["proCancel"]:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "High Allprotection mode on at : " +str(ginfo.name)
                                  else:
                                       Zie["proCancel"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "High Allprotection mode on at : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["proqr"]:
                                         del Zie["proqr"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Zie["proKick"]:
                                         del Zie["proKick"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Zie["proInvite"]:
                                         del Zie["proInvite"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Zie["proJoin"]:
                                         del Zie["proJoin"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Zie["proCancel"]:
                                         del Zie["proCancel"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protection mode off at : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protection mode off at : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「off mode」\n\n" + msgs)

                        elif 'Inta ' in msg.text:
                           if msg._from in Ley:
                              spl = msg.text.replace('Inta ','')
                              if spl == 'on':
                                  if msg.to in Zie["intaPoint"]:
                                       msgs = "Inta on"
                                  else:
                                       Zie["intaPoint"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "IntaPoint on at Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Zie["intaPoint"]:
                                         del Zie["intaPoint"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Intapoint off at Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Inta off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif ("Bot kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           cl.sendMessage(msg.to, "sorry bocah lu,,gw kick..!!!")
                                           random.choice(Amin).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z1 kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           Zie["pCancel"][msg.to] = True
                                           Zie["pInvite"][msg.to] = True
                                           Zie["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           ka.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z2 kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           Zie["pCancel"][msg.to] = True
                                           Zie["pInvite"][msg.to] = True
                                           Zie["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           kb.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z3 kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           Zie["pCancel"][msg.to] = True
                                           Zie["pInvite"][msg.to] = True
                                           Zie["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           kc.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z4 kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           Zie["pCancel"][msg.to] = True
                                           Zie["pInvite"][msg.to] = True
                                           Zie["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           kd.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z5 kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           Zie["pCancel"][msg.to] = True
                                           Zie["pInvite"][msg.to] = True
                                           Zie["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           ke.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Kiss " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Kicker kick " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ti = cl.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ti)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           X = k1.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           k1.updateGroup(X)
                                           k1.leaveGroup(msg.to)
                                       except:
                                           pass

                        elif ("Cancel" in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "empty ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Lea and x not in Fia["Bots"] and x not in Fia ["admin"]:
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "done.")

                        elif ("Bot cancel" in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "empty ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Lea and x not in Fia["Bots"] and x not in Fia ["admin"]:
                                       random.choice(Amin).cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "done.")

                        elif ("Addadmin " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Fia["admin"][target] = True
                                           f=codecs.open('Znfbot.json','w','utf-8')
                                           json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           cl.sendMessage(msg.to,"Succes add admin")
                                       except:
                                           pass

                        elif ("Addbot " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Fia["Bots"][target] = True
                                           f=codecs.open('Znfbot.json','w','utf-8')
                                           json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           cl.sendMessage(msg.to,"Succes add bot")
                                       except:
                                           pass

                        elif ("Deladmin " in msg.text):
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                        try:
                                            del Fia["admin"][target]
                                            f=codecs.open('Znfbot.json','w','utf-8')
                                            json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            cl.sendMessage(msg.to,"Succes delete admin")
                                        except:
                                            pass

                        elif ("Delbot " in msg.text):
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Lea:
                                        try:
                                            del Fia["Bots"][target]
                                            f=codecs.open('Znfbot.json','w','utf-8')
                                            json.dump(Fia, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            cl.sendMessage(msg.to,"Succes delete bots")
                                        except:
                                            pass

                        elif cmd == "botlist" or text.lower() == 'bot list':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              if Fia["Bots"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ Bot List ❳☚\n╠══════════════"
                                  for mi_d in Fia["Bots"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "adminlist" or text.lower() == 'admin list':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              if Fia["admin"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ Admin List ❳☚\n╠══════════════"
                                  for mi_d in Fia["admin"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in Ley:
                                Alfiah["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "admin:del" or text.lower() == 'admin:del':
                            if msg._from in Ley:
                                Alfiah["deladmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "admin:off" or text.lower() == 'admin off':
                            if msg._from in Ley:
                                Alfiah["addadmin"] = False
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "deladmin:off" or text.lower() == 'deladmin off':
                            if msg._from in Ley:
                                Alfiah["deladmin"] = False
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "bot:on" or text.lower() == 'bot on':
                            if msg._from in Ley:
                                Alfiah["abots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "bot:off" or text.lower() == 'bot off':
                            if msg._from in Ley:
                                Alfiah["abots"] = False
                                cl.sendMessage(msg.to,"done boss")

                        elif cmd == "bot:del" or text.lower() == 'bot del':
                            if msg._from in Ley:
                                Alfiah["dbots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "allrefresh" or text.lower() == 'refresh':
                            if msg._from in Ley:
                                Alfiah["addadmin"] = False
                                Alfiah["deladmin"] = False
                                Alfiah["abots"] = False
                                Alfiah["dbots"] = False
                                Alfiah["ablacklist"] = False
                                Alfiah["dblacklist"] = False
                                Alfiah["Tablacklist"] = False
                                Alfiah["Tdblacklist"] = False
                                cl.sendMessage(msg.to,"done bosquh")

                        elif cmd == "ctadmin" or text.lower() == 'ctadmin':
                            if msg._from in Ley:
                                ma = ""
                                for i in Fia["admin"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "ctbot" or text.lower() == 'ctbot':
                            if msg._from in Ley:
                                ma = ""
                                for i in Fia["Bots"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "notag:on" or text.lower() == 'notag on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag allready on")

                        elif cmd == "notag:off" or text.lower() == 'notag off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["Mentionkick"] = False
                                cl.sendMessage(msg.to,"Notag allready off")

                        elif cmd == "contact:on" or text.lower() == 'contact on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["contact"] = True
                                cl.sendMessage(msg.to,"Contact allready on")

                        elif cmd == "contact:off" or text.lower() == 'contact off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["contact"] = False
                                cl.sendMessage(msg.to,"Contact allready off")

                        elif cmd == "respon:on" or text.lower() == 'respon on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto allready on")

                        elif cmd == "respon:off" or text.lower() == 'respon off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon allready off")

                        elif cmd == "autojoin:on" or text.lower() == 'autojoin on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin allredy on")

                        elif cmd == "autojoin:off" or text.lower() == 'autojoin off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin allready off")

                        elif cmd == "scan:on" or text.lower() == 'scan on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["checkmid"] = True
                                cl.sendMessage(msg.to," allredy on")

                        elif cmd == "scan:off" or text.lower() == 'scan off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["checkmid"] = False
                                cl.sendMessage(msg.to," allready off")

                        elif cmd == "post:on" or text.lower() == 'post on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["checkPost"] = True
                                cl.sendMessage(msg.to,"Check Post allredy on")

                        elif cmd == "post:off" or text.lower() == 'post off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["checkPost"] = False
                                cl.sendMessage(msg.to,"Check Post allready off")

                        elif cmd == "unsend:on" or text.lower() == 'unsend on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["Unsend"] = True
                                cl.sendMessage(msg.to,"Detect unsend allredy on")

                        elif cmd == "unsend:off" or text.lower() == 'unsend off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["Unsend"] = False
                                cl.sendMessage(msg.to,"Detect unsend allready off")

                        elif cmd == "autoleave:on" or text.lower() == 'autoleave on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave allready on")

                        elif cmd == "autoleave:off" or text.lower() == 'autoleave off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave allready off")

                        elif cmd == "autoadd:on" or text.lower() == 'autoadd on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add allready on")

                        elif cmd == "autoadd:off" or text.lower() == 'autoadd off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add allready off")

                        elif cmd == "sticker:on" or text.lower() == 'sticker on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["sticker"] = True
                                cl.sendMessage(msg.to,"Sticker allready on")

                        elif cmd == "sticker:off" or text.lower() == 'sticker off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["sticker"] = False
                                cl.sendMessage(msg.to,"Sticker alleady off")

                        elif cmd == "jticket:on" or text.lower() == 'jticket on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket allready on")

                        elif cmd == "jticket:off" or text.lower() == 'jticket off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag allready off")

                        elif ("Tban " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Fia["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succses")
                                       except:
                                           pass

                        elif ("Untban " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Fia["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif cmd == "tban:on" or text.lower() == 'tban:on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["Tablacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "untban:on" or text.lower() == 'untban:on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["Tdblacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif ("Ban " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Zie["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Zie["blacklist"][target]
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["ablacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "ban:off" or text.lower() == 'ban off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["ablacklist"] = False
                                cl.sendMessage(msg.to,"done boss")

                        elif cmd == "unban:on" or text.lower() == 'unban on':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "unban:off" or text.lower() == 'unban off':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                                Alfiah["dblacklist"] = False
                                cl.sendMessage(msg.to,"done boss")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              if Zie["blacklist"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ BanList ❳☚\n╠══════════════"
                                  for mi_d in Zie["blacklist"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "tbanlist" or text.lower() == 'tbanlist':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              if Zie["Talkblacklist"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ BanList ❳☚\n╠══════════════"
                                  for mi_d in Zie["Talkblacklist"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "cban" or text.lower() == 'cban':
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              Zie["blacklist"] = {}
                              Zie["pCancel"] = {}
                              Zie["pInvite"] = {}
                              Zie["pQr"] = {}
                              ang = cl.getContacts(Zie["blacklist"])
                              mc = "%i Blacklist " % len(ang)
                              cl.sendMessage(msg.to,"done boss " +mc)

                        elif text.lower() == ".respon" or text.lower() == "respon.":
                            if msg._from in Ley:
                                if msg.to not in Zie["proCancel"] or msg.to not in Zie["proInvite"]:
                                    cl.sendMessage(msg.to, "stay boss")
                                else:
                                    del Zie["pCancel"][msg.to]
                                    del Zie["pInvite"][msg.to]
                                    del Zie["pQr"][msg.to]
                                    f=codecs.open('Znfblacklist.json','w','utf-8')
                                    json.dump(Zie, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ka.send(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    kb.send(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    kc.send(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    kd.send(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")
                                    ke.send(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴")

                        elif 'Add: ' in msg.text:
                           if msg._from in Ley:
                              ang = msg.text.replace('Add: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Alfiah["message"] = ang
                                  cl.sendMessage(msg.to, "「Msg add」 :\n\n「{}」".format(str(ang)))

                        elif 'Left: ' in msg.text:
                           if msg._from in Ley:
                              ang = msg.text.replace('Left: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Alfiah["leftmsg"] = ang
                                  cl.sendMessage(msg.to, "「Msg leave」 :\n\n「{}」".format(str(ang)))

                        elif 'Welcome: ' in msg.text:
                           if msg._from in Ley:
                              ang = msg.text.replace('Welcome: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Alfiah["welcome"] = ang
                                  cl.sendMessage(msg.to, "「Msg wellcome」 :\n\n「{}」".format(str(ang)))

                        elif 'Tag: ' in msg.text:
                           if msg._from in Ley:
                              ang = msg.text.replace('Tag: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Alfiah["msgTag"] = ang
                                  cl.sendMessage(msg.to, "「Msg tag」:\n\n「{}」".format(str(ang)))

                        elif 'Spam: ' in msg.text:
                           if msg._from in Ley:
                              ang = msg.text.replace('Spam: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Alfiah["spamMsg"] = ang
                                  cl.sendMessage(msg.to, "「Msg spam」 :\n\n「{}」".format(str(ang)))

                        elif 'Sider: ' in msg.text:
                           if msg._from in Ley:
                              znf = msg.text.replace('Sider: ','')
                              if znf in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Alfiah["siderMsg"] = znf
                                  cl.sendMessage(msg.to, "「Msg cctv」:\n\n「{}」".format(str(znf)))

                        elif text.lower() == "cekmsg":
                            if msg._from in Ley:
                               cl.sendMessage(msg.to, "「Msg add」 :\n「 " + str(Alfiah["message"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg cctv」:\n「 " + str(Alfiah["siderMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg tag」:\n「 " + str(Alfiah["msgTag"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg spam」:\n「 " + str(Alfiah["spamMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg welcome」:\n「 " + str(Alfiah["welcome"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg leave」:\n「 " + str(Alfiah["leftmsg"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "succes join : %s" % str(group.name))

                        elif ("Cleanse" in msg.text):
                          if Alfiah["selfbot"] == True:
                            if msg._from in Ley:
                               if msg.toType == 2:
                                  group = cl.getGroup(msg.to)
                                  group = ka.getGroup(msg.to)
                                  group = kb.getGroup(msg.to)
                                  group = kc.getGroup(msg.to)
                                  group = kd.getGroup(msg.to)
                                  group = ke.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                      if x not in Lea:
                                          if x not in Fia["Bots"]:
                                              if x not in Fia["admin"]:
                                                  try:
                                                      klist=[ka,kb,kc,kd,ke]
                                                      ang=random.choice(klist)
                                                      ang.kickoutFromGroup(msg.to,[x])
                                                  except:
                                                      print ("limit")
                        elif msg.text.lower() in ["check"]:
                            if msg._from in Ang:
                                anu = cl.getGroup(msg.to)
                                oncom = ["uafee8af1c47101fa12ae93e28da1ec80"] #MID PUSKUN
                                for _mid in oncom:
                                    message="╭━ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ━─\n"
                                    try:
                                        cl.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Kick\n"
                                    except:
                                        message+="│「☹ Limit」Kick\n"
                                    try:
                                        ka.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Invite\n"
                                    except:
                                        message+="│「☹ Limit」Invite\n"
                                    try:
                                        kb.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Kick\n"
                                    except:
                                        message+="│「☹ Limit」Kick\n"
                                    try:
                                        kc.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Invite\n"
                                    except:
                                        message+="│「☹ Limit」Invite\n"
                                    try:
                                        kd.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Kick\n"
                                    except:
                                        message+="│「☹ Limit」Kick\n"
                                    try:
                                        ke.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Invite\n"
                                    except:
                                        message+="│「☹ Limit」Invite\n"
                                    message+="╰━━━━━━━━─"
                                    cl.sendMessage(msg.to,message)
#=====================#
    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
