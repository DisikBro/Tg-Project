import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

load_dotenv()
apikey = os.getenv('apikey')

attraction_ids = []
city_ids = []


async def start(update, context):
    await update.message.reply_text(
        'Добро пожаловать! Это бот - Mr. Достопримечательный. Я покажу самые интересные '
        'достопримечательности в выбранном вами городе!\n'
        'Какой город вас интересует?', reply_markup=ReplyKeyboardRemove()
    )
    return 1


async def get_attractions(update, context):
    locality = update.message.text
    first_request = f'https://catalog.api.2gis.com/2.0/region/search?q={locality}&key={apikey}'
    first_response = requests.get(first_request).json()
    city_id = first_response['result']['items'][0]['id']
    city_ids.append(city_id)
    second_request = (f'https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id={city_id}'
                        f'&q=достопримечательности&key={apikey}')
    second_response = requests.get(second_request).json()
    for i in range(4):
        attraction_ids.append(second_response['result']['items'][i]['id'])
    await update.message.reply_text(attraction_ids)

    await update.message.reply_text(
        "Какие достопримечательности вас интересуют?", reply_markup=markup)


async def observation_platforms(update, context):
    rubric_items = []
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_ids[0]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                rubric_items.append(third_response['result']['items'][i][j])
    await update.message.reply_text('Вот список смотровых площадок')
    for i in rubric_items:
        await update.message.reply_text(i)


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


reply_keyboard = [['/observation_platforms', '/fountains'],
                  ['/interesting_buildings', '/natural_attractions']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
