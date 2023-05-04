import json
import requests
import telebot
from telebot import types
from mixins import  get_about_univers, get_all_news, get_retrieve_news, get_all_univers

HOST = 'http://13.51.255.44/'


Token = '6030590840:AAHPAHV-k4I-qa9E_Y5k35x6OBn6gUwv67M'

bot = telebot.TeleBot(Token)

auth_token = ''

def get_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Новости сайта', callback_data='news')
    button2 = types.InlineKeyboardButton(text='Университеты', callback_data='univer')
    keyboard.add(button1, button2)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!', reply_markup=get_keyboard())
    


@bot.callback_query_handler(func=lambda call: call.data == 'news')
def get_news(call):
    chat_id = call.message.chat.id
    news = get_all_news()
    keyboard = types.InlineKeyboardMarkup()

    for article in news:
        button = types.InlineKeyboardButton(text=article['title'],  callback_data='slug+'+article['slug'])
        keyboard.add(button)
    bot.send_message(chat_id, 'Вот новости на нашем сайте:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('slug+'))
def get_one_news(call):
    chat_id = call.message.chat.id
    slug = call.data.split('+')[1]
    news = get_retrieve_news(slug)
    bot.send_message(chat_id, text=f'{news["title"]}\nОписание: {news["description"]}\n\nhttp://13.51.255.44/article/{slug}')



@bot.callback_query_handler(func=lambda call: call.data == 'univer')
def get_univers(call):
    chat_id = call.message.chat.id
    news = get_all_univers()
    keyboard = types.InlineKeyboardMarkup()

    for univer in news:
        keyboard.add(types.InlineKeyboardButton(text=univer['name'], callback_data='id+'+str(univer['id'])))
    bot.send_message(chat_id, text='Список университетов:', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data.startswith('id+'))
def send_keyboard_message(call):
    chat_id = call.message.chat.id
    print(call.data)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Новости универа', callback_data='about_'+str(call.data.split('+'))[1]), types.InlineKeyboardButton(text='Об университете', callback_data='info_'+str(call.data.split('+')[1])))
    print(call.data.split('+')[1])
    bot.send_message(chat_id, text='Что хотите узнать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('id_un_'))
def get_about(call):
    chat_id = call.message.chat.id
    print(call.data)
    id = call.data.split('_')[2]
    info = get_about_univers(id)
    bot.send_message(chat_id, text=f'Название: {info.name}')

bot.polling()