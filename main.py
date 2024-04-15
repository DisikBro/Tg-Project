import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, filters, CommandHandler, CallbackContext, MessageHandler, ConversationHandler
from asyncs import *

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("observation_platforms", observation_platforms))
    application.add_handler(CommandHandler("fountains", fountains))
    application.add_handler(CommandHandler("interesting_buildings", interesting_buildings))
    application.add_handler(CommandHandler("natural_attractions", natural_attractions))
    application.add_handler(CommandHandler("close", close_keyboard))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_attractions)],
            2: []

        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
