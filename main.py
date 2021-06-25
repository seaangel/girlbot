import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('1882070325:AAHzt3_0YGEiHtVzA6ezXEmlwA496DfDRlg')

def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Покажи девушку')
  #  key2 = types.KeyboardButton('Текст второй кнопки')
    markup.add(key1)
  #  markup.add(key2)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, хочешь увидеть девушек, которые хотят познакомиться? Нажимай "Покажи девушку" и выбирай', reply_markup=main())

@bot.message_handler(content_types=['text'])
def cont(message):
    DIR = 'girl'
    with open ('text/text.txt', 'r',encoding="utf-8") as file:
        lines = file.readlines()
        life = random.choice(lines)
    boobs = str(random.randint(85,95))+'🍒'+' '+str(random.randint(60,70))+'⌛️'+' '+str(random.randint(80,100))+'🍑'
    adr = 'www.ya.ru'
    all_life = life +boobs +'\n'+'\n'+adr
    if message.text == 'Покажи девушку':
        
       # bot.send_photo(message.chat.id, open('girl/52LBCrywU28.jpg', 'rb'),caption='Ирина - 30 лет \n www.ya.ru')
        bot.send_photo(message.chat.id, open(os.path.join(DIR, random.choice(os.listdir(DIR))),'rb'),caption=all_life)
        #bot.send_message(message.chat.id, 'Ирина - 30 лет \n www.ya.ru', reply_markup=main())

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', reply_markup=main())

bot.polling()