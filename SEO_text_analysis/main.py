from load_data import *

vocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЁЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 0. получить текст
stext = getText()

# 1. заменить символы переноса на пробелы
ltext = list()
ltext += [lit if ord(lit) != 10 else ' ' for lit in stext]
stext = ''.join(ltext)

# 2. посчитать пробелы и буквы
ispaces = 0
ilits = 0
for lit in stext:
    if ord(lit) == 32:
        ispaces += 1
    if lit in vocab:
        ilits += 1


# 3. разделить на слова и удалить небуквы
lwords = stext.split(' ')
bufwords = list()  # временно
bufwords.extend(lwords)


# вывод
for i in stext:
    print(i, ord(i))
print(bufwords)
print()
print('Символов:                ', len(stext))
print('Символов ( без пробелов):', len(stext) - ispaces)
print('Букв:                    ', ilits)
print('Слов:                    ', len(bufwords))
