import locale
from datetime import datetime, date, timedelta
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

date_string = '01/01/25 12:10:03.234567'
format_datetime = date_string.replace('/', ' ').replace(':', ' ').replace(' ', ' ').replace('.', ' ').split()
print(format_datetime, type(format_datetime))
real_datetime = datetime(int(format_datetime[0]), int(format_datetime[0]), int(format_datetime[0]),
                         int(format_datetime[0]), int(format_datetime[0]),
                         int(format_datetime[0]), int(format_datetime[0]))
print(real_datetime)                # ЭТО УЖАСНЫЙ КОД, СОГЛАСЕН




