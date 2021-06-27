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
        name = 'Имя: ' + random.choice(lines)
    boobs = '\nРазмеры: '+str(random.randint(85,95))+'🍒'+' '+str(random.randint(60,70))+'⌛️'+' '+str(random.randint(80,100))+'🍑'
    age = 'Возраст: '+ str(random.randint(18,30))
    adr = 'https://vk.cc/c3dRgx'
    
    
    
    markup1 = telebot.types.InlineKeyboardMarkup()
    btn = [telebot.types.InlineKeyboardButton(text='🔥 Написать', url=adr),telebot.types.InlineKeyboardButton(text='➡️', callback_data='buy2')]
    
    markup1.add(*btn)
    
    
    all_life = name + age + boobs +'\n'+'\n'+adr
    if message.text == 'Покажи девушку':
        
       
        bot.send_photo(message.chat.id, open(os.path.join(DIR, random.choice(os.listdir(DIR))),'rb'),caption=all_life,reply_markup=markup1)
        

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', reply_markup=main())
        
#
      
@bot.callback_query_handler(func=lambda message:True)
def ans(message):
    cid = message.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    DIR = 'girl'
    with open ('text/text.txt', 'r',encoding="utf-8") as file:
        lines = file.readlines()
        name = 'Имя: ' + random.choice(lines)
    boobs = '\nРазмеры: '+str(random.randint(85,95))+'🍒'+' '+str(random.randint(60,70))+'⌛️'+' '+str(random.randint(80,100))+'🍑'
    age = 'Возраст: '+ str(random.randint(18,30))
    adr = 'https://vk.cc/c3dRgx'
    all_life = name + age + boobs +'\n'+'\n'+adr
    markup1 = telebot.types.InlineKeyboardMarkup()
    btn = [telebot.types.InlineKeyboardButton(text='🔥 Написать', url=adr),telebot.types.InlineKeyboardButton(text='➡️', callback_data='buy2')]
    
    markup1.add(*btn)
    if message.data == "buy2":
        #bot.send_message(cid, "Нажали 1-ю кнопку",reply_markup=keyboard)
        bot.send_photo(cid, open(os.path.join(DIR, random.choice(os.listdir(DIR))),'rb'),caption=all_life,reply_markup=markup1)
      
       
   
    
bot.polling()
