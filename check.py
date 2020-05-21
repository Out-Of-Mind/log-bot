import requests
from te_bot import Bot
import time
import pickle

bot = Bot("config.ini")

def check(address):
    try:
        r = str(requests.get(address).status_code)
    except:
        r = f'cannot get {address}'
        bot.send_message(602086212, r)

def main():
    while True:
        try:
            with open('w', 'rb') as f1:
                l = pickle.load(f1)
        except:
            l = []
        for i in l:
            check(i)
        time.sleep(15)
