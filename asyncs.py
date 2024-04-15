import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

load_dotenv()
apikey = os.getenv('apikey')


async def start(update, context):
    await update.message.reply_text(
        'Добро пожаловать! Это бот - Mr. Достопримечательный. Я покажу самые интересные '
        'достопримечательности в выбранном вами городе!\n'
        'Какой город вас интересует?'
    )
    return 1


async def get_attractions(update, context):

    locality = update.message.text
    # first_request = f'https://catalog.api.2gis.com/2.0/region/search?q={locality}&key={apikey}'
    # first_response = requests.get(first_request).json()
    # city_id = first_response['result']['items'][0]['id']
    # second_request = (f'https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id={city_id}'
    #                   f'&q=достопримечательности&key={apikey}')
    # second_response = requests.get(second_request).json()

    attraction_id = []

    await update.message.reply_text(
        "Какие достопримечательности вас интересуют?", reply_markup=markup)
    return 2


async def observation_platforms(update, context):
    await update.message.reply_text('observation_platforms')


async def fountains(update, context):
    await update.message.reply_text('fountains')


async def interesting_buildings(update, context):
    await update.message.reply_text('interesting_buildings')


async def natural_attractions(update, context):
    await update.message.reply_text('natural_attractions')


async def stop(update, context):
    await update.message.reply_text('Всего доброго!')
    return ConversationHandler.END


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


reply_keyboard = [['/1', '/2'],
                  ['/3', '/4']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
