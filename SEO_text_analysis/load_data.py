import collections
def file(text: str) -> str:
inp = input("Название файла: ")
f = open(inp, "r")
s = f.read().lower()
f.close()
text = "Кол-во символов: %s" % str(len(s))
text += "Кол-во символов (без пробелов): %s" % str(len(s.replace(" ", "")))
letters_d = {}
words = collections.Counter(s.split())
text += "Кол-во слов: %s" % str(len(s.split()))
for x in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
    letters_d[x] = 0
for x in s:
    if letters_d.get(x) != None:
        letters_d[x] += 1
search = sorted(letters_d.values())[-1]
numb = 0
for x in letters_d.values():
    numb+=int(x)
text += "Кол-во букв: %s" % str(numb)
for x, y in letters_d.items():
    if y == search:
        text += "Часто встречающаяся буква: %s" % x
text += "Часто встречающиеся слова: %s" % str(dict(words.most_common(10)))
