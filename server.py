from flask import Flask, request, jsonify
from te_bot import Bot
import main
import threading
import check

app = Flask(__name__)
bot = Bot('config.ini')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        main.main(chat_id, message, bot)
        return jsonify(r)
    else:
        return 'hi'

@app.route('/log', methods=['GET', 'POST'])
def lo():
    if request.method == 'POST':
        if request.headers['hjk']== 'UPj#*mUh:1%?k@ew':
            n = request.get_json()
            if n['s']:
                main.lo(n, bot)
            if n['ss']:
                bot.send_message(602086212, n['mes']+' from '+n['from'])
        return 'hi'
    else:
        return 'hi'

def m():
    e = threading.Thread(target=app.run, args=['127.0.0.1', 5000])
    r = threading.Thread(target=check.main)
    e.start()
    r.start()

if __name__ == '__main_':
    app.run(port=5002)
    
m()

