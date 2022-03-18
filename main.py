import requests
import time
import httpx
from colorama import Fore
import os
import sys
import string
import random, string
from discord import Webhook, RequestsWebhookAdapter


url = "https://spclient.wg.spotify.com/signup/public/v1/account"


headers = {
  'authority': 'spclient.wg.spotify.com',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'content-type': 'application/x-www-form-urlencoded',
  'accept': '*/*',
  'origin': 'https://www.spotify.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.spotify.com/',
  'accept-language': 'en-US,en;q=0.9'
}

g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
re = Fore.RESET
l = Fore.LIGHTBLACK_EX
blue = Fore.BLUE
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))



def drawsign():
    print(f'''
    
    {blue}




███╗░░██╗██╗████████╗██████╗░░█████╗░██╗░░░░░
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║██║░░░░░
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║██║░░░░░
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝███████╗
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝
                                                                                                                                       

Made by Cyxum#0001
If you need any help Contact me on discord Cyxum#0001

    {re}
    
    
    ''')





def mainfunctional():
    os.system("cls")
    drawsign()
    dhook = input(f'[{blue}DISCORD{re}] Webhook > ')
    recdata = {'content':'**NitroL** Succesfully Attached '}
    receiveme = httpx.post(dhook,json=recdata)
    os.system("cls")
    print(f"[{y}INITIALIZING{re}] Loading...")
    time.sleep(3)
    print(f'[{g}NitroL{re}] Starting Now')
    while True:
        Nitro = "https://discord.gift/"+random_char(16)
        accdata = {
        'content':f'**NitroL**\n{Nitro}'
     }
        sendacc = httpx.post(dhook,json=accdata)




        



    



if __name__ == '__main__':
    mainfunctional()
