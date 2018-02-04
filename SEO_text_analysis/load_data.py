# функция загрузки текста из файла
# input path
# output variable with text
def FileLoading(way):
    f = open(way, 'r')
    return f.read()
