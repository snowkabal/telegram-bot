import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import emoji

TOKEN = "5677493058:AAFBJC-C4mcyrhsBMvbQJ61xuuTPfPMf0zI"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome. To learn more about our software, Subscribe to this Channel!\n👉https://t.me/heetsbruteforcer4")

def generate_text(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a generated text.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text("Generate"), generate_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()