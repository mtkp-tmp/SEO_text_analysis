from load_data import getTextFromFile
import re

vocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'

# подготовка текста: убираются знаки переноса и лишние пробелы
def formatText(text):
    return ' '.join(text.split())

# буквы
def getLettersCount(text):
    text = text.lower()
    return sum([text.count(let) for let in set(text) if let in vocab])

# пробелы
def getSpaces(text):
    return text.count(' ')

# слова
def getWordCount(text):
    reg = re.compile('([^\.\s\,\;\:\!\?\'\"\{\}]+)')
    return len([word for word in reg.findall(text.lower()) if word != '-'])

# частые буквы
def getPopularLetters(text):
    text = text.lower()
    try:
        maxCount = max([text.count(let) for let in set(text) if let in vocab])
        return maxCount, [let for let in set(text) if text.count(let) == maxCount]
    except ValueError:  # нет букв
        return 0, ['в тексте нет букв']


# частые слова
def getPopularWords(text):
    reg = re.compile('([^\.\s\,\;\:\!\?\'\"\{\}]+)')
    wordList = [word for word in reg.findall(text.lower()) if word != '-']
    try:
        maxCount = max([wordList.count(word) for word in set(wordList)])  # находим максимальное вхождение
        return maxCount, [word for word in set(wordList) if wordList.count(word) == maxCount]
    except ValueError:  # нет слов
        return 0, ['в тексте нет слов']


try:
    # sText = getTextFromFile(input('Имя файла: '))
    sText = getTextFromFile('text.txt')
except FileNotFoundError:
    print('Файла не существует!')
else:
    if formatText(sText) != '':
        sText = formatText(sText)
        print('Символов:                ', len(sText))
        print('Символов (без пробелов): ', len(sText) - getSpaces(sText))
        print('Букв:                    ', getLettersCount(sText))
        print('Слов:                    ', getWordCount(sText))
        print('Частые слова:')
        wordCount, popularWords = getPopularWords(sText)
        for word in popularWords:
            print(' ', wordCount, '-', word)
        countLetters, popularLetters = getPopularLetters(sText)
        print('Частые буквы:')
        for let in popularLetters:
            print(' ', countLetters, '-', let)
    else:
        print('Файл пуст или состоит только из пробелов!')