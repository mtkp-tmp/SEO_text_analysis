from load_data import getTextFromFile
import re

class SEO_Analisys:
    vocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'

    def __init__(self, t):
        self.text = t.replace('\n', ' ')

    # символов
    def Length(self):
        return len(self.text)

    # символов без пробелов
    def LengthWithoutSpaces(self):
        return len(self.text) - self.text.count(' ')

    # буквы
    def LettersCount(self):
        return len(re.findall('\w', self.text))

    # количество слов
    def WordCount(self):
        return len([word for word in re.split('[^(\w+\-\w+)]', self.text.lower().replace(' - ', ' ')) if word != ''])

    # частые буквы
    def FrequentLetters(self):
        text = self.text.lower()
        try:
            maxCount = max([text.count(let) for let in set(text) if let in self.vocab])
            return maxCount, [let for let in set(text) if text.count(let) == maxCount]
        except ValueError:  # нет букв
            return 0, ['в тексте нет букв']

    # частые слова
    def FrequentWords(self):                    # разделение слов с учётом дефисов
        wordList = [word for word in re.split('[^(\w+\-\w+)]', self.text.lower().replace(' - ', ' ')) if word != '']
        try:
            maxCount = max([wordList.count(word) for word in set(wordList)])  # находим максимальное вхождение
            return maxCount, [word for word in set(wordList) if wordList.count(word) == maxCount]
        except ValueError:  # нет слов
            return 0, ['в тексте нет слов']


FILENAME = 'text.txt'
try:
    cText = SEO_Analisys(getTextFromFile(FILENAME))
    print('Символов:                ', cText.Length())
    print('Символов (без пробелов): ', cText.LengthWithoutSpaces())
    print('Букв:                    ', cText.LettersCount())
    print('Слов:                    ', cText.WordCount())
    print('Частые слова:')
    wordCount, popularWords = cText.FrequentWords()
    for word in popularWords:
        print(' ', wordCount, '-', word)
    countLetters, popularLetters = cText.FrequentLetters()
    print('Частые буквы:')
    for let in popularLetters:
        print(' ', countLetters, '-', let)
except FileNotFoundError:
    print('Файла не существует!')