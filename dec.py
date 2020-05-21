def command(str, f):
    def wrapper(func):
        def dec(chat_id, message, bot):
            if str in message:
                f(chat_id, message, bot)
            func(chat_id, message, bot)
        return dec
    return wrapper

def none():
    pass