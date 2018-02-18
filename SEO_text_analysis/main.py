from load_data import getTextFromFile

# подготовка текста: убираются знаки переноса и лишние пробелы
class SEO_Analisys:
    vocab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'

    def __init__(self, t):
        self.text = t

    def Length(self):
        return len(self.text)

    # буквы
    def LettersCount(self):
        text = self.text.lower()
        return sum([text.count(let) for let in set(text) if let in self.vocab])

    # пробелы
    def SpaceCount(self):
        return self.text.count(' ')

    # количество слов
    def WordCount(self):
        import re
        reg = re.compile('([^\.\s\,\;\:\!\?\'\"\{\}]+)')
        return len([word for word in reg.findall(self.text.lower()) if word != '-'])

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
        import re
        reg = re.compile('([^\.\s\,\;\:\!\?\'\"\{\}]+)')
        wordList = [word for word in reg.findall(self.text.lower()) if word != '-']
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
    print('Символов (без пробелов): ', cText.Length() - cText.SpaceCount())
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

