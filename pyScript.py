import re


def CLet_space(text=""):  # функция возвращает количество символов в тексте (c пробелами)
    return re.findall(r'.', text)


def CWord(text=""):  # функция количество слов в тексте
    return re.findall(r'\w+', text)


def CLet(text=""):  # функция возвращает количество символов в тексте (без пробелов)
    return re.findall(r'\S', ''.join(CLet_space(text)))


def CZed(text=""):  # функция возвращает количество букв в тексте
    return (re.findall(r'\D', ''.join(CLet(text))))


def oftenLetters(text=""):  # функция возвращает самое часто-встречающееся буква из текста

    maxCount = 0
    for symbol in CZed(text):
        if CZed(text).count(symbol) > maxCount:
            maxCount = CZed(text).count(symbol)
            maxLetter = symbol
    return maxLetter


def oftenWord(text=""):  # функция возвращает самое часто-встречающееся слово из текста

    maxCount = 0
    for word in CWord(text):
        if CWord(text).count(word) > maxCount:
            maxCount = CWord(text).count(word)
            maxWord = word
    return maxWord


path = input("Укажите путь к файлу: ")
try:
    with open(path, "r") as file:
        text = file.read()
        print('количество символов текста (с пробелами):', len(CLet_space(text)))
        print('количество символов текста (без пробелов):', len(CLet(text)))
        print('количество букв в тексте: ', len(CZed(text)))
        print('количество слов в тексте: ', len(CWord(text)))
        print("самая часто-встречающаяся буква: ", "'", oftenLetters(text), "'")
        print("самое часто-встречающееся слово из текста: ", "'", oftenWord(text), "'")
        file.close()

except FileNotFoundError:
    print("Такого файла не cуществует")
