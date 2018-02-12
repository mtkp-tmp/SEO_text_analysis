from re import *
from load_data import *
from os import *

# Функция вычисления количества символов и слов в тексте (без пробелов)
def CountSymbols(str):
    result1 = findall(r'[^  ]', str)

    result2 = findall(r'\w+', str)

    return (result1.__len__(), result2.__len__())

    # Функция вычисления количества букв в тексте
def SetLetter(str):
    result = findall(r'\w', str)
    return result.__len__()

    # Функция вычисления часто встречающейся буквы
def RepeatLetter(str):
    count = 1
    ch = ''
    dopsym = []
    # Сложный цикл для вычисления часто встречающейся буквы
    for i in str:
        ThisCount = 0
        for j in str:
            if (j != ' '):
                if ((j == i) | (j == i.upper())):
                    ThisCount += 1
        if (ThisCount > count):
            count = ThisCount
            ch = i
            # Добавления буквы в лист
    dopsym.append(ch)
    # Поиск подобных букв по количеству вхождений
    for i in str:
        ThisCount = 0
        for j in str:
            if (j != ' '):
                if ((j == i) | (j == i.upper())):
                    ThisCount += 1
        if ((ThisCount == count) & (i not in dopsym)):
            dopsym.append(i)

    return dopsym

    # Функция вычисления часто встречающегося слова
def RepeatWord(str):
    symb = {'.', ',', '!', '?', ':', ';', ' '}
    lst = []
    slovo = ''
    # Цикл разбиения текста на слова и запись их в лист
    for i in str:
        if (((ord(i) > 64) & (ord(i) < 91) | (ord(i) > 96) & (ord(i) < 123) | (ord(i) > 1039) & (ord(i) < 1104))):
            slovo += i.lower()

        if i in symb:
            if slovo != '':
                lst.append(slovo)
                slovo = ''
                # Цикл вычисления часто встречающегося слова
    count = 0
    slovo = ''
    dopwords = []
    for i in lst:
        Ncount = 0
        Ncount = lst.count(i)
        if (Ncount > count):
            count = Ncount
            slovo = i

    dopwords.append(slovo)

    for i in lst:
        ThisCount = 0
        ThisCount = lst.count(i)
        if (i != slovo) & (ThisCount == count) & (i not in dopwords):
            dopwords.append(i)
    return dopwords


                # Проверка введённого пути
f = True
while(f):
    put = input("Введите путь к файлу с текстом: ")
    if (access(put, F_OK) == True):
        f = False
    else:
        print("Ошибка! Неверный путь к текстовому файлу! Пожалуйста, повторите ввод.")

str = FileLoading(put)


print(str)
CountWords = 0
CountSymbolP = 0
# Кол-во символов в тексте (с пробелами)
print("Кол-во символов (с пробелами): ", str.__len__())
CountSymbolP, CountWords = CountSymbols(str)
print("Кол-во символов (без пробелов): ", CountSymbolP)
print("Кол-во букв в тексте: ", SetLetter(str))
print("Кол-во слов в тексте: ", CountWords)
print("Самая часто-встречающаяся буква: ", RepeatLetter(str))
print("Самое часто-встречающееся слово: ", RepeatWord(str))
