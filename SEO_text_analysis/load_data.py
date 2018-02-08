# функция загрузки текста из файла
# input path
# output variable with text


def getTextFromFile(path):
    # return open(input('Имя файла: '), 'r').read()
    return open(path, 'r').read()