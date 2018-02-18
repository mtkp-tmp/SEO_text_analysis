from load_data import getTextFromFile
import re
# подготовка текста: убираются знаки переноса и лишние пробелы
class SEO_Analisys:
    vocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'

    def __init__(self, t):
        self.text = t

    # символов
    def Length(self):
        return len(self.text)

    # символов без пробелов
    def LengthWithoutSpaces(self):
        return len(self.text) - self.text.count(' ')

    # буквы
    def LettersCount(self):
        text = self.text.lower()
        return sum([text.count(let) for let in set(text) if let in self.vocab])

    # количество слов
    def WordCount(self):
        return len(re.split('\W+', self.text)) - 1

    # частые буквы
    def FrequentLetters(self):
        text = self.text.lower()
        try:
            maxCount = max([text.count(let) for let in set(text) if let in self.vocab])
            return maxCount, [let for let in set(text) if text.count(let) == maxCount]
        except ValueError:  # нет букв
            return 0, ['в тексте нет букв']

    # частые слова
    def FrequentWords(self):
        wordList = re.split('\W+', self.text.lower())
        try:
            maxCount = max([wordList.count(word) for word in set(wordList)])  # находим максимальное вхождение
            return maxCount, [word for word in set(wordList) if wordList.count(word) == maxCount]
        except ValueError:  # нет слов
            return 0, ['в тексте нет слов']


FILENAME = 'text.txt'

try:
    cText = SEO_Analisys(getTextFromFile(FILENAME))
except FileNotFoundError:
    print('Файла не существует!')
else:
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


ttt = 'Из-за шкафа показался бело-черный кот. Он странно выглядел. Он - я.'

print(re.split('\W+', ttt))