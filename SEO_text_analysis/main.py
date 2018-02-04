from load_data import *
# без оптимизации
sVocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЁЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 0. получить текст
sText = getText()

# 1. заменить символы переноса на пробелы
lText = list()
lText += [lit if ord(lit) != 10 else ' ' for lit in sText]
sText = ''.join(lText)

# 2. удалить лишние пробелы и разделить на слова
lWords = sText.split()
sText = ' '.join(lWords)

# 3. посчитать пробелы и буквы
iSpaces = 0
iLits = 0
for lit in sText:
    if lit in sVocab:
        iLits += 1
    elif ord(lit) == 32:
        iSpaces += 1

# 4. удалить небуквы и неслова
# lWords = [word.lower() if word[len(word)-1] in sVocab else word[0:-1].lower() for word in lWords] устраревший, не удалялись многоточия
lWords = [word.lower() if (word[len(word)-1] in sVocab) & (word[0] in sVocab) else ''.join([w for w in word if w in sVocab]).lower() for word in lWords]
lWords = [word for word in lWords if word != '']

# 5. популярные слова
lPopWords = list()


# вывод
for i in sText:
    print(i, ord(i))
print(lWords)
print()
print('Символов:                ', len(sText))
print('Символов (без пробелов): ', len(sText) - iSpaces)
print('Букв:                    ', iLits)
print('Слов:                    ', len(lWords))
