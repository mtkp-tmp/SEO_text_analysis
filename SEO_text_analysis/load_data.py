from re import compile, findall
f = open(input("Введите путь к файлу для чтения "), "r")
str = f.read()
letters, count_let, max_let, count_w, max_w = len(str), 0, "", 0, ""
for i in str :
    if not i.isalpha(): letters -= 1 #вычитаем не буквы из всех символов
print(str) #строка
print(len(str)) #кол-во символов
print(len(str.replace(' ', ''))) #кол-во символов без пробела
print(letters) #кол-во букв
print(len((compile(r'\w+')).findall(str))) #кол-во слов
for let in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz" : #буква из строки
    if count_let < (str.lower()).count(let): count_let, max_let = (str.lower()).count(let), let
print(max_let) #самая встречающаяся буква
for w in (compile(r'\w+')).findall(str):
    if count_w < (compile(r'\w+')).findall(str).count(w): count_w, max_w = (compile(r'\w+')).findall(str).count(w), w #слово из всех слов
print(max_w) #самое встречающееся слово
