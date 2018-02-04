# функция загрузки текста из файла
# input path
# output variable with text


def getText():
    print('Имя файла: ')
    # file = open(input(), 'r')
    file = open('text.txt', 'r')
    return file.read()
