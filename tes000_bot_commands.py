
from re import U
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater, MessageHandler, ConversationHandler
import datetime
from log import*
from random import randint

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/info\n/help\n/candy')
    
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
    
async def plus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    item = msg.split()
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    item = msg.split()
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')
    
async def mult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    item = msg.split()
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} - {y} = {x*y}')

async def div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    item = msg.split()
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} - {y} = {x/y}')

def msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = int(item[1])
    return x
    

async def info(update, context):
    await context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды для вычислений:
                             /sum x y   = сумма х,у
                             /minus x y   = разность х,у
                             /mult x y   = произведение х,у
                             /div x y   = деление х/у""")    
    
    
    
# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

async def candy(update, context):
    await context.bot.send_message(update.effective_chat.id,
    """Игра - конфеты!
    Условия игры: На столе лежит 2021 конфета.
    Игрок против бота.
    Первый ход определяется автоматической жеребьёвкой.
    За один ход можно забрать не более чем 28 конфет.
    Тот, кто берет последнюю конфету - проиграл.""")

    candy_amount = 2021
    await context.bot.send_message(update.effective_chat.id,
                             """Игроку для ввода набрать - /msg x , где x - кол-во конфет.""")


    
    hod = randint(1, 11)
    


    if hod <= 5:
        await context.bot.send_message(update.effective_chat.id,
                             """Первым ходит игрок1""")
        hod = 1
    else:
        await context.bot.send_message(update.effective_chat.id,
                             """Первым ходит игрок2""")
        hod = 2

    while candy_amount >= 1:
        if hod == 1:
            await context.bot.send_message(update.effective_chat.id,
                             """Ваш ход, возьмите от 1 до 28 конфет""")
            
            candy1 = msg(update, context)
                        
            if 0 < candy1 < 29:
                candy_amount = candy_amount - candy1
                if candy_amount < 1:
                    await context.bot.send_message(update.effective_chat.id,
                             """Вы проиграли!""")
                    quit()
                await context.bot.send_message(update.effective_chat.id,
                             f'Осталось конфет - {candy_amount}')
                hod = 2
        if hod == 2:
            candy2 = (candy_amount - 30) % 29
            if candy2 == 0:
                candy2 = randint(1, 29)
            if candy_amount <= 29:
                candy2 = candy_amount-1
            if 0 < candy2 < 29:
                candy_amount = candy_amount - candy2
                await context.bot.send_message(update.effective_chat.id,
                             f'бот взял - {candy2}')
                if candy_amount < 1:
                    await context.bot.send_message(update.effective_chat.id,
                             """Бот проиграл!""")
                    quit()
                await context.bot.send_message(update.effective_chat.id,
                             f'Осталось конфет - {candy_amount}')
                hod = 1
