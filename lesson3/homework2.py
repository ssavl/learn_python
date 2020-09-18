import csv


lst = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('homework.csv', 'w', encoding='utf-8') as mycsv:
    # format_cntnt = str(f'{lst[0]["name"]} : {lst[0]["age"]} : {lst[0]["job"]}')
    # print(format_cntnt)
    content = mycsv.write(str(lst).replace(',' ,':'))