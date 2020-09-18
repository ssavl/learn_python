
with open('referat.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(len(content))


count_words = str(content)
print(len(set(count_words.split())))


ln = content.replace('.', '!')
print(ln)


with open('referat.txt', 'w', encoding='utf-8') as savefile:
    content2 = savefile.write(ln)



