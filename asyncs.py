from telegram.ext import ConversationHandler


async def start(update, context):
    await update.message.reply_text(
        'Добро пожаловать! Это бот - Mr. Достопримечательный. Я покажу самые интересные'
        'достопримечательности в выбранном вами городе!\n'
        'Какой город вас интересует?'
    )
    return 1


async def first_response(update, context):
    locality = update.message.reply_text
    await update.message.reply_text(
        f'Вот достопримечательности в городе {locality}'
    )
    return 2


async def stop(update, context):
    await update.message.reply_text('Всего доброго!')
    return ConversationHandler.END
