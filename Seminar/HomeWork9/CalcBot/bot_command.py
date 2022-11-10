from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, Я калькулятор-бот!Введите команду "/go" и через пробел числа и действие, которое хотите выполнить (+,-,*,/) ')

 
async def calculater(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split() 
    x = int(items[1])
    y = int(items[2])
    if items[3]=='+':
        await update.message.reply_text(f'Результат: {x+y}')
    if items[3]=='-':
        await update.message.reply_text(f'Результат: {x-y}') 
    if items[3]=='*':
        await update.message.reply_text(f'Результат: {x*y}')  
    if items[3]=='/':
        await update.message.reply_text(f'Результат: {x/y}')  