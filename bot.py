#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice
import json


#my id, replace it with yours.
owner = 845646704
ignored = []
#730069224:AAF9ShPFniRtS7voRhtejgPOcFoQaHapUhg
token = '736244244:AAHlPRDrgRRRnwekYiT19oZDFuo-I84aNAw'
bot = telebot.TeleBot("736244244:AAHlPRDrgRRRnwekYiT19oZDFuo-I84aNAw")
welcome_message = '''
Olá, eu sou bot contato, eu sou um bot feito para você entrar em contato
com meu proprietário, apenas emita o texto como usual, eu respondê-lo-ei tão rapidamente quanto posible!.
'''
infobot = bot.get_me()
bot_nome = infobot.first_name
user_bot = infobot.username
bot_id = infobot.id
#Custom listener.
#It logs all messages to console.
def listener(messages):
   for m in messages:
      cid = m.chat.id
      if(m.content_type == 'text'):
          if cid > 0:
             name = m.chat.first_name.encode('ascii', 'ignore').decode('ascii')
             mensaje = name + "["+str(cid) + "]:" + m.text
          else:
             name = m.from_user.first_name.encode('ascii', 'ignore').decode('ascii')
             mensaje = name + "["+str(cid)+"]:"+ m.text
          print(mensaje.encode('ascii', 'ignore').decode('ascii'))

#Create Bot.
bot = telebot.TeleBot(token)
print('Username:[' + user_bot + ']')
#Set custom listener.
bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def ign(m):
    if(not m.from_user.id == owner):
        return
    if(m.reply_to_message):
        i = m.reply_to_message.from_user.id
        name = m.reply_to_message.from_user.first_name
        ignored.append(i)
        bot.reply_to(m, "user {}[{}] ignored.".format(name, i))
    else:
        bot.reply_to(m, 'Olá, eu sou bot contato, eu sou um bot feito para você entrar em contato*')
    
#Deep Linking handler
@bot.message_handler(commands=['start'])
def start(m):
    if(not m.from_user.id == owner):
        name = m.from_user.first_name
        uid = m.from_user.id
        bot.send_message(uid, welcome_message)
        bot.send_message(owner, "Usuário {}[{}] iniciou o bot.".format(name, uid))


#About message.
@bot.message_handler(commands=['help'])
def about(m):
    cid = m.chat.id
    bot.send_message(cid, "Created by @Fraviiu", parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def forward(m):
    uid = m.from_user.id
    if(m.reply_to_message and uid == owner):
        try:
            bot.send_message(m.reply_to_message.forward_from.id, m.text)
        except:
            bot.send_message(owner, 'O usuário bloqueou o bot.')
    if(not uid == owner):
        bot.forward_message(owner, m.from_user.id , m.message_id)
#Bot starts here.
bot.polling(True)
