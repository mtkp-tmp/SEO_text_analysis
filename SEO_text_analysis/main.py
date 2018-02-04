from load_data import *

vocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЁЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 0. получить текст
stext = getText()

# 1. заменить символы переноса на пробелы
ltext = list()
ltext += [lit if ord(lit) != 10 else ' ' for lit in stext]
stext = ''.join(ltext)

# 2. удалить лишние пробелы и разделить на слова
lwords = stext.split()
stext = ' '.join(lwords)
bufwords = list()  # для сравнения изменений
bufwords.extend(lwords)

# 3. посчитать пробелы и буквы
ispaces = 0
ilits = 0
for lit in stext:
    if lit in vocab:
        ilits += 1
    elif ord(lit) == 32:
        ispaces += 1

# 4. удалить небуквы и неслова
newlwords = list()
newlwords = [word.lower() if word[len(word)-1] in vocab else word[0:-1].lower() for word in lwords]

# вывод
for i in stext:
    print(i, ord(i))
print(bufwords)
print(newlwords)
print()
print('Символов:                ', len(stext))  # 156 прав
print('Символов ( без пробелов):', len(stext) - ispaces)
print('Букв:                    ', ilits)
print('Слов:                    ', len(bufwords))
