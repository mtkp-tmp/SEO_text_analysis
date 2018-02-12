import re


def TexWithoutSpace(s):
    return len(s)


def TextWithSpace(s):
    return len(''.join(s.split()))


def CountLetter(s):
    return (sum([1 for elem in s.lower() if elem in local]))


def CountWord(s):
    reg = re.compile('([^\.\s\,\;\:\!\?\'\"\{\}]+)')
    return len([1 for elem in reg.findall(s.lower()) if elem != '-'])


def PopularLetter(s):
    MaxLetter = max([s.count(elem) for elem in s if elem in local])
    return MaxLetter, [elem for elem in set(s) if s.count(elem) == MaxLetter]


def PopularWord(s):
    reg = re.compile('([^\.\s\,\;\:\!\?\'\"\{\}]+)')
    listword = [elem for elem in reg.findall(s.lower()) if elem != '-']
    maxword = max([listword.count(elem) for elem in set(listword)])
    return maxword, [elem for elem in set(listword) if listword.count(elem)== maxword]


local = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
f = open('C:/Users/Владислав/Desktop/Just_a_text.txt')
s = (f.read())
print(s)

WithoutSpace = print(TexWithoutSpace(s))
WithSpace = print(TextWithSpace(s))
letters = print(CountLetter(s))
Words = print(CountWord(s))
PopularLetters = print(PopularLetter(s))
PopularWords = print (PopularWord(s))
