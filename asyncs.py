import os
import random

import requests
from yamager import Yamager
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from data import db_session

from data.ids import Ids
from data.names import Names

load_dotenv()
apikey = os.getenv('apikey')

city_ids = []
info = []
third_response1 = []


async def start(update, context):
    await update.message.reply_text(
        'Добро пожаловать! Это бот - Mr. Достопримечательный. Я покажу самые интересные '
        'достопримечательности в выбранном вами городе!\n', reply_markup=ReplyKeyboardMarkup([['/LES_GO']])
    )


async def start_2(update, context):
    await update.message.reply_text('Какой город вас интересует?', reply_markup=ReplyKeyboardRemove())
    return 1


async def get_attractions(update, context):

    locality = update.message.text
    first_request = f'https://catalog.api.2gis.com/2.0/region/search?q={locality}&key={apikey}'
    first_response = requests.get(first_request).json()
    if len(first_response) > 1:
        city_id = first_response['result']['items'][0]['id']
        city_ids.append(city_id)
        second_request = (f'https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id={city_id}'
                          f'&q=достопримечательности&key={apikey}')
        second_response = requests.get(second_request).json()
        for i in range(4):
            db_sess = db_session.create_session()
            ids = db_sess.query(Ids).filter(Ids.id == int(i + 1)).first()
            ids.attraction_id = second_response['result']['items'][i]['id']
            db_sess.add(ids)
            db_sess.commit()
        await update.message.reply_text(
            "Какие достопримечательности вас интересуют?", reply_markup=markup)
        return 2
    else:
        await update.message.reply_text('Введите корректный город!')
        return 1


async def observation_platforms(update, context):
    db_sess = db_session.create_session()
    attraction_id = db_sess.query(Ids.attraction_id).filter(Ids.id == 1).first()
    db_sess.query(Names).filter(Names.id >= 1).delete()
    db_sess.commit()
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_id[0]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                name = Names()
                name.name = third_response['result']['items'][i][j]
                db_sess.add(name)
                db_sess.commit()
    attraction_names = db_sess.query(Names.name).all()
    if attraction_names:
        await update.message.reply_text('Вот список смотровых площадок:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in attraction_names:
            await update.message.reply_text(i[0])
        await update.message.reply_text('Пожалуйста выберите интересующую вас')
        return 2
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')


async def fountains(update, context):
    db_sess = db_session.create_session()
    attraction_id = db_sess.query(Ids.attraction_id).filter(Ids.id == 2).first()
    db_sess.query(Names).filter(Names.id >= 1).delete()
    db_sess.commit()
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_id[0]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                name = Names()
                name.name = third_response['result']['items'][i][j]
                db_sess.add(name)
                db_sess.commit()
    attraction_names = db_sess.query(Names.name).all()
    if attraction_names:
        await update.message.reply_text('Вот список фонтанов:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in attraction_names:
            await update.message.reply_text(i[0])
        await update.message.reply_text('Пожалуйста выберите интересующий вас')
        return 2
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')


async def interesting_buildings(update, context):
    db_sess = db_session.create_session()
    attraction_id = db_sess.query(Ids.attraction_id).filter(Ids.id == 3).first()
    db_sess.query(Names).filter(Names.id >= 1).delete()
    db_sess.commit()
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_id[0]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                name = Names()
                name.name = third_response['result']['items'][i][j]
                db_sess.add(name)
                db_sess.commit()
    attraction_names = db_sess.query(Names.name).all()
    if attraction_names:
        await update.message.reply_text('Вот список интересных зданий:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in attraction_names:
            await update.message.reply_text(i[0])
        await update.message.reply_text('Пожалуйста выберите интересующее вас')
        return 2
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')


async def natural_attractions(update, context):
    db_sess = db_session.create_session()
    db_sess.query(Names).filter(Names.id >= 1).delete()
    db_sess.commit()
    attraction_id = db_sess.query(Ids.attraction_id).filter(Ids.id == 4).first()
    third_requests = (f'https://catalog.api.2gis.com/3.0/items?rubric_id='
                      f'{attraction_id[0]}&region_id={city_ids[0]}&key={apikey}')
    third_response = requests.get(third_requests).json()
    third_response1.append(third_response)
    for i in range(len(third_response['result']['items'])):
        for j in third_response['result']['items'][i]:
            if j == 'building_name':
                name = Names()
                name.name = third_response['result']['items'][i][j]
                db_sess.add(name)
                db_sess.commit()
    attraction_names = db_sess.query(Names.name).all()
    if attraction_names:
        await update.message.reply_text('Вот список природных достопримечательностей:',
                                        reply_markup=ReplyKeyboardRemove())
        for i in attraction_names:
            await update.message.reply_text(i[0])
        await update.message.reply_text('Пожалуйста выберите интересующую вас')
        return 2
    else:
        await update.message.reply_text('К сожалению достопримечательностей в данной категории нет,'
                                        ' попробуйте другую категорию')


async def get_info(update, context):
    info1 = []
    db_sess = db_session.create_session()
    attraction_names = db_sess.query(Names.name).all()
    building = update.message.text
    for i in attraction_names:
        if building.lower() == i[0].lower():
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
        await update.message.reply_text('Данных о достопримечательности не найдено ^_^, но есть картинка!)')
    info.clear()
    third_response1.clear()
    city_ids.clear()
    yan = Yamager()
    images = []
    for i in range(2):
        image = yan.search_google_images(str(building))
        images.append(image)
    for i in range(len(images) + 1):
        await update.message.reply_photo(random.choice(images[i]))
    await update.message.reply_text('Выберем другой город? Выбора не дано!',
                                    reply_markup=ReplyKeyboardMarkup([['/da']]))
    return 3


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
