from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('db.csv', 'a') as file:
        file.write(f'{datetime.datetime.now().time()}; {update.effective_user.first_name}; {update.effective_user.id}; {update.message.text}\n')