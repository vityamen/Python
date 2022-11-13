from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from bot_command import hello

from bot_command import calculater

app = ApplicationBuilder().token("токен").build()
app.add_handler(CommandHandler("hello", hello)))
app.add_handler(CommandHandler('go', calculater))
print('server start)')

app.run_polling()