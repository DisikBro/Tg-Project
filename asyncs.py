import os

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
    await update.message.reply_text(
        f"Вот некоторые достопримечательности в городе {locality}")
    return 2


async def second_response(update, context):
    await update.message.reply_text(
        f"Что бы вы хотели узнать о {}"
    )


async def stop(update, context):
    await update.message.reply_text('Всего доброго!')
    return ConversationHandler.END
