import os

import telebot
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from telebot import types

from manager.models import Manager
from realty.models import Realty

# parsing()

import time

# from tbot.parser.parser import parsing

# import schedule
import time

bot = telebot.TeleBot(settings.BOT_TOKEN)
webhook_address = settings.TELEGRAM_BOT_WEBHOOK_URL

bot.remove_webhook()
bot.set_webhook(webhook_address)


# Флаг, чтобы проверить, был ли установлен вебхук
webhook_set = False

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    return HttpResponse('<h1>Bot live!</h1>')


# Кнопка "START"
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Последние добавленные квартиры")
    item2 = types.KeyboardButton("Все квартиры")
    item3 = types.KeyboardButton("Контакты менеджеров")
    item4 = types.KeyboardButton("Наш сайт")
    item5 = types.KeyboardButton("Крыша")
    item6 = types.KeyboardButton("-----")

    markup.row(item1, item2)
    markup.row(item3, item4)
    markup.row(item5, item6)

    bot.send_message(message.chat.id,
                     "Привет! Это бот сайта недвижимости, выберете в меню интересующие вас пункты!",
                     reply_markup=markup)


# Кнопка "Все квартиры"
@bot.message_handler(func=lambda message: message.text == "Все квартиры")
def all_apartments(message):
    # Замените URL ниже на вашу реальную ссылку
    link = "https://example.com/all_apartments"
    bot.send_message(message.chat.id, f"Вот ссылка на все квартиры: {link}")


# Кнопка "Последние добавленные квартиры"
@bot.message_handler(func=lambda message: message.text == "Последние добавленные квартиры")
def latest_apartments(message):
    apartments = Realty.objects.filter(active=True).order_by('-id')[:5]

    for apartment in apartments:
        txt = f"Тип: {apartment.type_realty}\n"
        txt += f"Заголовок: {apartment.title}\n"
        txt += f"Площадь: {apartment.s} м²\n"
        txt += f"Комнат: {apartment.rooms}\n"
        txt += f"Информация: {apartment.info}\n"
        txt += f"Цена: {apartment.price} руб.\n"

        # Добавляем ссылку на объект недвижимости на вашем сайте
        website_link = f"https://yourwebsite.com/realty/{apartment.id}"  # Замените на реальный URL
        txt += f"Ссылка на объект: {website_link}\n"

        # Отправляем сообщение с информацией о квартире и вставленной фотографией
        bot.send_photo(message.chat.id, apartment.cover_image, caption=txt)


# Кнопка 'Контакты менеджеров'
@bot.message_handler(func=lambda message: message.text == "Контакты менеджеров")
def manager_contacts(message):
    managers = Manager.objects.all()

    for manager in managers:
        txt = f"Имя: {manager.name}\n"
        txt += f"Телефон: {manager.phone}\n"
        txt += f"Email: {manager.email}\n"

        bot.send_message(message.chat.id, txt)


# Кнопка "Наш сайт"
@bot.message_handler(func=lambda message: message.text == "Наш сайт")
def all_apartments(message):
    # Замените URL ниже на вашу реальную ссылку
    link = "https://example.com/all_apartments"
    bot.send_message(message.chat.id, f"Вот ссылка на наш сайт: {link}")# Кнопка "Наш сайт"


# @bot.message_handler(func=lambda message: message.text == "Крыша")
# def all_apartments(message):
#     # Замените URL ниже на вашу реальную ссылку
#     link = "test button"
#
#     new_flats = parsing()
#
#     for flat in new_flats:
#         txt = f"link: https://krisha.kz{flat}\n"
#         txt += f"info: {new_flats[flat][0]}\n"
#         txt += f"price: {new_flats[flat][1]}\n"
#         txt += f"\n"
#
#         bot.send_message(message.chat.id, txt)


# test
def my_test_view(new_flats):

    chat_id = "180958616"  # Замените на идентификатор чата, куда нужно отправить сообщение

    if len(new_flats) == 0:
        bot.send_message(chat_id, 'Обновлений нет')

    else:
        for flat in new_flats:
            txt = f"link: https://krisha.kz{flat}\n"
            txt += f"info: {new_flats[flat][0]}\n"
            txt += f"price: {new_flats[flat][1]}\n"
            txt += f"\n"
            bot.send_message(chat_id, txt)







def telegram_page_views(request):
    return render(request, 'bot.html')