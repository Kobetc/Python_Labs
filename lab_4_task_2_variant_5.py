import os.path
import re

# Путь к файлу с русским текстом
filePath = "./lab_4_task_2_variant_5.txt"
# Регулярное выражение определяющее символы в строке, которые не входят в диапазон А-яЁё
regexForCyrilicSymbol = re.compile('[^А-яЁё]')


def getData(filePath):

    charsCount = 0              # Счетчик русских символов в тексте
    # Словарь, ключами которого станут символы, а значение - число символов в тексте
    symbolsDictionary = {}

    # Проверяем, существует ли файл по переданному пути filePath
    if not os.path.exists(filePath):
        return {"symbolsDictionary": symbolsDictionary, "charsCount": charsCount}

    # Читаем файл
    inputFile = open(filePath, mode="r", encoding="utf-8")

    for line in inputFile.readlines():   # Чтение файла по строкам
        # Перебор символов в строке из которой убраны все символы, кроме кирилицы (пробелы, числа, точки, запятые)
        for char in regexForCyrilicSymbol.sub("", line):

            charsCount = charsCount + 1

            if char not in symbolsDictionary:   # Если символ встретился в тексте первый раз
                # В словаре создается новый ключ, значение равно 1
                symbolsDictionary[char] = 1
            else:
                # Ксли в словаре уже есть ключ равный символу, т.е. символ уже встречался в тексте
                # Прибавляем к значению по ключу 1
                symbolsDictionary[char] = symbolsDictionary[char] + 1

    # Закрываем файл
    inputFile.close()

    # Возвращаем словарь, с разбитыми на ключи по символам из текста файла и число русских символов в тексте
    return {"symbolsDictionary": symbolsDictionary, "charsCount": charsCount}


symbolsData = getData(filePath)
symboslCount = symbolsData["charsCount"]
symbolsDictionary = symbolsData["symbolsDictionary"]

# Проходим по все ключам/символам в словаре
for symbol in symbolsDictionary:

    # Процент вычисляется как значение из словаря по ключу/символу, означающего число раз, сколько символ встретился в тексте
    # помноженное на 100% и деленное на общее число символов в тексте
    procent = symbolsDictionary[symbol] * 100 / symboslCount

    print(symbol, " - ", procent, "% от", symboslCount, "символов")
