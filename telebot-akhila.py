!pip install adafruit-io
x = "akhilagadhiraju" #ADAFRUIT_IO_USERNAME
y = "aio_WwAR11pGL8kQId6scOdAIbnA3VtH" #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(x,y)
result = aio.create_feed(new)
from Adafruit_IO import Data
!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('bot',Data(value = 1))
  bot.send_message(chat_id =chat_id,text ="Lights On")

def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('bot',Data(value = 0))
  bot.send_message(chat_id =chat_id,text ="Lights Off")

updater = Updater('1399714177:AAHs--Y_1lJc-zwIUomPcn50cQbMrVwzris')     #Use Telegram Token HTTP API
dp =updater.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()
updater.idle()
