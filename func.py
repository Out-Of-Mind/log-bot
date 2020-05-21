import requests
import pickle

def start(chat_id, message, bot):
    bot.send_message(chat_id, 'hi')

def watch(chat_id, message, bot):
    bot.send_message(chat_id, 'ok')
    try:
        r = requests.get(message[7:])
        r = r.status_code
        try:
            with open('w', 'wb') as f, open('w', 'rb') as f1:
                l = pickle.load(f1)
                l.append(message [7:])
                pickle.dump(l, f)
        except:
            with open('w', 'wb') as f:
                pickle.dump([message[7:]], f)
    except Exception as e:
        print(e)
        r = 'cannot ping'
    bot.send_message(chat_id, str(r))

def stop(chat_id, message, bot):
    with open('w', 'rb') as f:
            l = pickle.load(f)
            try:
                l.remove(message[6:])
                bot.send_message(chat_id, 'stopped watching {}'.format(message[6:]))
            except:
                bot.send_message(chat_id, "cannot stop, because this url isn't watching")
    with open('w', 'wb') as f:
            pickle.dump(l, f)

def help(chat_id, message, bot):
    bot.send_message(chat_id, '/stop url - to stap watching,\n/watch url - to watch url')