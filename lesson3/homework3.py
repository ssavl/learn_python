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
date_dt = datetime.strptime(date_string, '%m/%d/%Y ')
print(date_dt)




