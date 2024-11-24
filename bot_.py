import telebot as tb

bot = tb.TeleBot("BOT_TOKEN") #необходимо указать токен

def send_msg_(chatid, text_msg):
    bot.send_message(chat_id=chatid, text=text_msg)

@bot.message_handler(commands=["add_id"])
def add_id(message):
    with open(file="ids.txt", mode="a", encoding="utf-8") as user_ids:
        user_ids.write(f"{message.chat.id}\n")
    bot.send_message(chat_id=message.chat.id, text=f"ID {message.chat.id} зарегистрирован.")



