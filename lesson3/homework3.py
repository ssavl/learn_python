import locale
from datetime import datetime, date, timedelta
import time
"""Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime"""
dt_now = datetime.now()
delta = timedelta(days=1)
delta1 = timedelta(days=30)
locale.setlocale(locale.LC_TIME, 'ru_RU')

# today
print(dt_now)

# yesterday
print(dt_now - delta)

# 30 days ago
print(dt_now - delta1)

# str to datatime

date_string1 = '01/01/25 12:10:03.234567'
real_datetime = datetime.strptime(date_string1, "%d/%m/%y %H:%M:%S.%f") # Очень долго искал на какую букву форматируется миллисекунды
print(real_datetime, type(real_datetime))


