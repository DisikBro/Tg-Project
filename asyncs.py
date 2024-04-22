import os
import random

import requests
from yamager import Yamager
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

load_dotenv()
apikey = os.getenv('apikey')

attraction_ids = []
city_ids = []
info = []
rubric_items = []
third_response1 = []


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
    await update.message.reply_text(city_id)
    second_request = (f'https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id={city_id}'
                      f'&q=достопримечательности&key={apikey}')
    second_response = requests.get(second_request).json()
    for i in range(4):
        attraction_ids.append(second_response['result']['items'][i]['id'])
    await update.message.reply_text(
        "Какие достопримечательности вас интересуют?", reply_markup=markup)
    return 2


async def observation_platforms(update, context):
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_ids[0]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                rubric_items.append(third_response['result']['items'][i][j])
    if rubric_items:
        await update.message.reply_text('Вот список смотровых площадок:')
        for i in rubric_items:
            await update.message.reply_text(i)
        await update.message.reply_text('Пожалуйста выберите интересующую вас')
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')
    return 2


async def fountains(update, context):
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_ids[1]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                rubric_items.append(third_response['result']['items'][i][j])
    if rubric_items:
        await update.message.reply_text('Вот список фонтанов:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in rubric_items:
            await update.message.reply_text(i)
        await update.message.reply_text('Пожалуйста выберите интересующую вас')
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')
    return 2


async def interesting_buildings(update, context):
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_ids[2]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                rubric_items.append(third_response['result']['items'][i][j])
    if rubric_items:
        await update.message.reply_text('Вот список интересных зданий:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in rubric_items:
            await update.message.reply_text(i)
        await update.message.reply_text('Пожалуйста выберите интересующую вас')
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')
    return 2


async def natural_attractions(update, context):
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_ids[3]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                rubric_items.append(third_response['result']['items'][i][j])
    if rubric_items:
        await update.message.reply_text('Вот список природных достопримечательностей:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in rubric_items:
            await update.message.reply_text(i)
        await update.message.reply_text('Пожалуйста выберите интересующую вас')
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')
    return 2


async def get_info(update, context):
    info1 = []
    building = update.message.text
    for i in rubric_items:
        if building.lower() == i.lower():
            for j in range(len(third_response1[0]['result']['items'])):
                for k in third_response1[0]['result']['items'][j]:
                    if k == 'building_name':
                        if building.lower() == third_response1[0]['result']['items'][j][k].lower():
                            info.append(third_response1[0]['result']['items'][j])
    for i in info:
        info1.extend([i['address_name'], i['building_name'], i['full_name'], i['purpose_name']])
    if info1:
        for i in range(len(info1)):
            await update.message.reply_text(info1[i])
    else:
        await update.message.reply_text('Данных о достопримечательности не найдено ^_^')
    info.clear()
    rubric_items.clear()
    third_response1.clear()
    attraction_ids.clear()
    city_ids.clear()
    yan = Yamager()
    images = yan.search_google_images(str(building))
    return random.choice(images)
    # await update.message.reply_text('Выберем другой город?',
    #                                 reply_markup=ReplyKeyboardMarkup([['/on_start']]))


async def on_start(update, context):
    await update.message.reply_text('Какой город вас интересует?', reply_markup=ReplyKeyboardRemove())

    return 1


# async def search_photo(query):
#     try:
#         yan = Yamager()
#         images = yan.search_google_images(str(query))
#         # prprprpr
#         return random.choice(images)
#     except Exception as e:
#         return str(e)


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
