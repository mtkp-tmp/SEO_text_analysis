f = open('test.txt')
data = f.read().lower()
print('Количество символов текста (с пробелами) : ' + str(len(data)))
print('Количество символов текста (без пробелов) : ' + str(len(data.replace(' ', ''))))
print('Количество букв в тексте : ' + str(len([i for i in data if i.isalpha()])))
print('Количество слов в тексте : ' + str(len(data.split())))
print('Самая часто-встречающаяся буква : ' + 
	str([key + ' встречается в файле ' + str(value) + ' раз' for key, value in sorted(dict(zip([i for i in data if i.isalpha()], 
		[data.count(i) for i in data if i.isalpha()])).items(), key=lambda item: (item[1], item[0]))][-1]))
print(['Самое часто-встречающееся слово : ' + key + ' встречается в файле ' + str(value) + ' раз' for key, value in sorted(dict(zip([w for w in ''.join([l  if l.isalpha() | l.isspace() else ' ' for l in data]).split()],
	[[w for w in ''.join([l  if l.isalpha() | l.isspace() else ' ' for l in data]).split()].count(w) for w in [w for w in ''.join([l  if l.isalpha() | l.isspace() else ' ' for l in data]).split()]])).items(), key=lambda item: (item[1],item[0]))][-1])

f.close()

