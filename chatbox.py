import configparser
import telegram
from telegram.ext import Updater, MessageHandler, Filters
import logging

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
                        level=logging.INFO)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update:" + str(update))
    logging.info("context" + str(update))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

if __name__=='__main__':
    main()

