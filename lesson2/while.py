"""Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соответствующий ответ. Например:
"""

import random


def ask_user(answer1, answer2):
    while True:
        dct = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", 'Сколько времени сейчас?':'не знаю'}
        answers = ["Извини, спрошу еще раз", 'Понимаю, а если подумать о хорошем?']
        ask = str(input("Как дела?")).lower()
        if ask == 'хорошо':
            ask1 = str(input('Спроси меня о чем нибудь!'))
            if ask1 in dct:
                print(dct[ask1])
            else:print('круто было поговорить))')
        else: print(random.choice(answers))


ask_user('хорошо', "Что делаешь?")