import json
import telebot
from pprint import pprint as pp

from bot_state import State

if __name__ == '__main__':
   with open('conf.cfg', 'r') as fele:
      config = json.loads(fele.read())

   bot = telebot.TeleBot(config['token'])
   state = State()


   @bot.message_handler(func = lambda message: (message.text in ('рус', 'укр')) and (state.now == state._reset) )
   def set_lang ( message):
      state.change(state._start)
      state.set_lang(message.text)
      bot.send_message ( message.chat.id, 'выбрали %s и поехали'%state.lang)
      pass


















   @bot.message_handler(commands = ['start', 'reset'])
   def greetings ( message):

      state.set_lang(None)
      state.change(state._reset)

      markup = telebot.types.ReplyKeyboardMarkup(
         resize_keyboard = True,
         one_time_keyboard = True
      )
      markup.row(
         telebot.types.KeyboardButton('рус'),
         telebot.types.KeyboardButton('укр')
      )

      bot.send_message ( 
         message.chat.id, 
         'Выберите язык/Оберіть мову', 
         reply_markup = markup )

   @bot.message_handler(content_types = ['text'])
   def wrong_command ( message):
      bot.send_message ( 
         message.chat.id,
         {
            'рус':'Неверная команда "%s". Попробуйте вновь или /reset.'%message.text,
            'укр':'Невірна команда "%s". Спробуйте знову або /reset.'%message.text,
            'NOT_SET':'Wrong command "%s". Try again or /reset.'%message.text
         }[state.lang]
         
      )
      pass
   
   bot.polling()
   