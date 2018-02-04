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
lWords = [word.lower() if (word[len(word)-1] in sVocab) & (word[0] in sVocab) else ''.join([w for w in word if w in sVocab]).lower() for word in lWords]
lWords = [word for word in lWords if word != '']


# 5. нахождение элементов списка с максимальным вхождением
def getMaxIn(lSource):
    lPopWords = list()
    iPopWords = list()
    for word in lSource:
        if word in lPopWords:
            iPopWords[lPopWords.index(word)] += 1
        else:
            lPopWords.append(word)
            iPopWords.append(1)
    iCount = 0
    for i in iPopWords:
        if i > iCount:
            iCount = i
    return [lPopWords[i] for i in range(0, len(lPopWords)) if iPopWords[i] == iCount], iCount


lPopWords, iWordCount = getMaxIn(lWords)
lPopLits, iLitCount = getMaxIn(''.join(sText.split()))

# вывод
print('Символов:                ', len(sText))
print('Символов (без пробелов): ', len(sText) - iSpaces)
print('Букв:                    ', iLits)
print('Слов:                    ', len(lWords))
print('Частые слова:')
for word in lPopWords:
    print(' ', word, '-', iWordCount)
print('Частые буквы:')
for lit in lPopLits:
    print(' ', lit, '-', iLitCount)
