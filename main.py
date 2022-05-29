import telebot
import json

bot = telebot.TeleBot('5542786377:AAFMlTF7svHMVm_USSQeWITtudq60wVyUbY')

@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id ,"Привет " + message.from_user.first_name + ", напишите что-нибудь...")

@bot.message_handler()
def getUserText(message):
    if message!='/start':
        if checkWord(message.text):
            bot.send_message(message.chat.id, "you banned!")
            bot.ban_chat_sender_chat(message.chat.id,message.from_user.id)
        else:
            bot.send_message(message.chat.id, "not banned")


def checkWord(text):
    f = open('venv/word.json')

    data = json.load(f)
    text = text.lower()
    user_text = text.split(' ')
    for i in data:
        word = i["fields"]["word"]

        if word in user_text:
            return True

    f.close()
    return False


bot.polling(none_stop=True)
