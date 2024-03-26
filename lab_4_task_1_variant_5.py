import os.path

fileAPath = "./27-166a.txt"
fileBPath = "./27-166b.txt"


def getData(filePath):

    dataLen = 0
    minMinutes = 0
    data = []

    # Проверяем, существует ли файл по переданному пити filePath
    if not os.path.exists(filePath):
        return {"dataLen": dataLen, "minMinutes": minMinutes, "data": data}

    # Читаем файл
    # Разбиваем файл по строкам и получаем список
    # Закрываем файл
    inputFile = open(filePath)
    fileLines = inputFile.readlines()
    inputFile.close()

    # Первую строку считанную из файла очищаем от символа перевода каретки и символа новой строки и разбиваем по пробелу, получая список
    # Первый элемент полученного списка - N - количество переданных показаний
    # Второй элемент списка - K - минимальное количество минут, которое должно пройти между моментами передачами любых двух из трёх показаний.
    try:
        dataParams = fileLines[0].rstrip("\r \n").split(" ")
        dataLen = (int(dataParams[0]))
        minMinutes = (int(dataParams[1]))

    except IndexError:
        print("Файл не содержит строк или в первой строке не два слова !")

    except ValueError:
        print("Первая строка не содержит чисел !")

    # Строки считанные из файла, начиная со 2-й (индекс 1), очищаем от символа перевода каретки и символа новой строки
    # преобразовываем в число и добавляем в список data
    for line in fileLines[1:]:
        try:
            data.append(int(line.rstrip("\r \n")))

        except:
            print("Строка не содержит число !")

    # Возвращаем словарь, с разбитыми на ключи данными из файла
    return {"dataLen": dataLen, "minMinutes": minMinutes, "data": data}


print(getData(fileAPath))
