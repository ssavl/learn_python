import random


def ask_user(answer1, answer2):
    try:
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

    except KeyboardInterrupt:
            print('Пока!')




ask_user('хорошо', "Что делаешь?")