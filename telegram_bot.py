from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from tes000_bot_commands import*



app = ApplicationBuilder().token('5655137944:AAGnw142E4eCC50Fe_GQBPJvEwZTpYOmh_k').build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("sum", plus))
app.add_handler(CommandHandler("minus", minus))
app.add_handler(CommandHandler("mult", mult))
app.add_handler(CommandHandler("div", div))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("start", info))
app.add_handler(CommandHandler("candy", candy))
app.add_handler(CommandHandler("msg", msg))


print('server starts')
#app.updater.idle()
app.run_polling()

