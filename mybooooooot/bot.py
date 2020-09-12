from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
import time


time = str(datetime.datetime.now()).split()
print(time[0])
mars = ephem.Mars(time[0])
var =  ephem.constellation(mars)
print(var)


logging.basicConfig(filename='bot.log', level=logging.INFO)
token = '588416825:AAG56Akr2blqglSC8SuIAuAVr3K7lCeQNe0'




def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Hi i am a smart bot! write me the name of any planet in the solar system '
                              'and I will tell you its coordinates for today 😂 Just write to me  and the name of the '
                              'planet 🪐')


def talk_to_me(update, context):
    user_text = str(update.message.text).capitalize()
    print(user_text)
    if user_text == 'Mars':
        planet = getattr(ephem, user_text)
        update.message.reply_text(planet(time))
    # if user_text == 'Mercury':
    #     update.message.reply_text(f'Ты хочешь узнать кординаты {getattr(ephem, user_text)}')
    # if user_text == 'Earth':
    #     update.message.reply_text(f'Ты хочешь узнать кординаты {user_text}  на {time[0]} ?')
    # if user_text == 'Saturn':
    #     update.message.reply_text(f'Ты хочешь узнать кординаты {user_text}  на {time[0]} ?')
    # if user_text == 'Venus':
    #     update.message.reply_text(f'Ты хочешь узнать кординаты {user_text}  на {time[0]} ?')

    else: update.message.reply_text('ошибка')


def main():
    mybot = Updater(token, use_context=True)
    md = mybot.dispatcher
    md.add_handler(CommandHandler("start", greet_user))
    md.add_handler(MessageHandler(Filters.text, talk_to_me))
    print('starting...')
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


main()