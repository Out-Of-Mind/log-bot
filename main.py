import func
from dec import command
import pickle

@command('/help', func.help)
@command('/start', func.start)
@command('/watch', func.watch)
@command('/stop', func.stop)
def main(chat_id, message, bot):
    print('main')

def lo(n, bot):
    with open('w', 'rb') as f:
        l = pickle.load(f)
        l.append(n['host'])
    with open('w', 'wb') as f:
        pickle.dump(l, f)
    bot.send_message(602086212, 'start watching {}'.format(n['host']))