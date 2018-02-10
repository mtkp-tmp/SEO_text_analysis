from load_data import getTextFromFile

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
    wordList = text.lower().split()
    wordList = [word if (word[-1] in vocab) & (word[0] in vocab) else ''.join(
        [w for w in word if w in vocab]) for word in wordList]
    wordList = [word for word in wordList if word != '']
    return len(wordList)

# частые буквы
def getPopularLetters(text):
    text = text.lower()
    try:
        maxCount = max([text.count(let) for let in set(text) if let in vocab])
    except ValueError:  # нет букв
        return 0, ['в тексте нет букв']
    else:
        return maxCount, [let for let in set(text) if text.count(let) == maxCount]

# частые слова
def getPopularWords(text):  # второй метод
    # форматирование слов: удаление запятых, многочий, тире и тд
    # слова с дефисом не трогаются
    wordList = text.lower().split()
    wordList = [word if (word[-1] in vocab) & (word[0] in vocab) else ''.join(
        [w for w in word if w in vocab]) for word in wordList]
    wordList = [word for word in wordList if word != '']
    try:
        maxCount = max([wordList.count(word) for word in set(wordList)])  # находим максимальное вхождение
    except ValueError:  # нет слов
        return 0, ['в тексте нет слов']
    else:
        return maxCount, [word for word in set(wordList) if wordList.count(word) == maxCount]


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
