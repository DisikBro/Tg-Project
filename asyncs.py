import os

import requests
from dotenv import load_dotenv
from telegram.ext import ConversationHandler

load_dotenv()
apikey = os.getenv('apikey')


async def first_response(update, context):
    await update.message.reply_text(
        'Добро пожаловать! Это бот - Mr. Достопримечательный. Я покажу самые интересные '
        'достопримечательности в выбранном вами городе!\n'
        'Какой город вас интересует?'
    )
    return 1


async def get_attractions(update, context):

    locality = update.message.text
    first_request = f'https://catalog.api.2gis.com/2.0/region/search?q=Миасс&key={apikey}'
    first_response = requests.get(first_request).json()
    city_id = first_response['result']['items'][0]['id']
    second_request = (f'https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id='
                       f'{city_id}&q=достопримечательности&key={apikey}')
    second_response = requests.get(second_request).json()
    attraction_id = [

    ]
    await update.message.reply_text(
        f"Вот некоторые достопримечательности в городе {locality}")
    return 2


# async def second_response(update, context):
#     await update.message.reply_text(
#         f"Что бы вы хотели узнать о {}"
#     )


async def stop(update, context):
    await update.message.reply_text('Всего доброго!')
    return ConversationHandler.END
