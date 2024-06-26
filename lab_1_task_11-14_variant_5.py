

inputStringForTasks = ("Натуральные числа — числа, получаемые при естественном счёте: N = { 1 , 2 , 3 , . . . }. Иногда к множеству натуральных чисел также относят ноль, то есть N = { 0 , 1 , 2 , 3 , . . . }.\n"
                       "Целые числа — числа, получаемые объединением натуральных чисел со множеством чисел противоположных натуральным и нулём, обозначаются Z = { . . . − 2 , − 1 , 0 , 1 , 2 , . . . }.\n"
                       "Рациональные числа — числа, представимые в виде дроби m/n (n ≠ 0), где m — целое число, а n — натуральное число.\n"
                       "Действительные (вещественные) числа — числа, представляющие собой расширение множества рациональных чисел, замкнутое относительно некоторых (важных для математического анализа) операций предельного перехода.\n"
                       "Комплексные числа — числа, являющиеся расширением множества действительных чисел. Они могут быть записаны в виде z = x + i y, где i — т. н. мнимая единица, для которой выполняется равенство i 2 = − 1.")


#
# Задача 2. Отсортировать строки в указанном порядке: В порядке увеличения среднего веса ASCII-кода символа строки.
#


def averageWeightSymbols(inputString):

    # Список, в который будем помещать элементы типа (Средний вес ASCII-кода символа строки,  строка)
    stringWithASCIIList = []

    # Проходим по списку состоящиму из строк
    for string in inputString.split("\n"):

        # Определяем число символов в строке
        stringLen = len(string)

        # Инициализируем сумму всех ASCII кодов символов строки
        summASCIICodes = 0

        # Проходим по символам строки
        for char in string:

            # Определяем ASCII код символа
            asciiCode = ord(char)

            # Суммируем с общей суммой
            summASCIICodes = summASCIICodes + asciiCode

        try:
            # Определяем среднее значение ASCII кода в строке. Сумма кодов всех символов строки на число символов в строке
            # Используем try, для защиты от деления на 0
            averageWeightOfString = summASCIICodes // stringLen
        except:
            pass

        # Добавляем в список элемент (отределенное среднее значение. сама строка)
        stringWithASCIIList.append((averageWeightOfString, string))

    # Сортируем список по первому значению в элементе списка, т.е по среднему значению ASCII-кода символа строки
    sortedStringList = sorted(stringWithASCIIList, reverse=False)

    # Проходим по списку, формируем список состоящий только из вторых элементов, т.е. самих строк,
    # и склеиваем их через символ новой строки \n
    outputString = "\n".join(string
                             for (len, string) in sortedStringList)

    print("Результат работы:")
    print("")

    print("Исходная строка: ")
    print("")
    print(inputString)
    print("")
    print("Отсортированная строка: ")
    print("")
    print(outputString)

    return

#
# Задача 6. В порядке увеличения медианного значения выборки строк (прошлое
#           медианное значение удаляется из выборки и производится поиск нового медианного значения).
#


# Нахождение медианного значения ASCII кодов символов строки
def getMedianOfStringByASCII(string):

    # Длина строки
    lenOfString = len(string)

    # Список, в который будут помещены ASCII коды символов строки
    asciiList = []

    # Расчитанное медианное значение ASCII кодов символов строки
    medianOfStringByASCII = 0

    # Заполняем список ASCII кодами символов строки
    for char in string:
        asciiList.append(ord(char))

    # Сортируем список с кодами по возрастанию
    sortedAsciiList = sorted(asciiList)

    # Если длина строки делится на два без остатка, значит длина - четное число
    if lenOfString % 2 == 0:

        # Берем два центральных элемента списка
        twoCenterItems = sortedAsciiList[(
            lenOfString // 2 - 1):(lenOfString // 2 + 1)]

        # Определяем среднее арифметическое медлу двумя центральными элементами, это будет медиальным значением
        medianOfStringByASCII = sum(twoCenterItems) // 2
    else:
        # Если длина строки не четное число, берем центральный элемент списка, это будет медиальным значением
        centerItem = sortedAsciiList[lenOfString // 2]
        medianOfStringByASCII = centerItem

    # Возвращаем найденное медианное значение ASCII кодов символов строки
    return medianOfStringByASCII


def stringsMedian(inputString):

    # Список, куда будут помещаться строки по мере сортировки
    outputStringsList = []

    # Полученная строка с отсортированными подстроками
    outputString = ""

    # Разбиваем строки по символу новой строки - \n
    stringsList = inputString.split("\n")

    # Определяем начальное количество строк в наборе строк
    lenStringsList = len(stringsList)

    # Запускаем цикл столько раз, сколько строк в наборе строк
    for startIndex in range(lenStringsList):

        # Производим выборку строк от startIndex до конца списка stringsList
        sliceOfStrings = stringsList[startIndex:]

        # Список, в который будем помещать медианные значения строк из выборки и строку. В виде элементов (медианное значение, строка)
        stringsWithMediansList = []

        # Проходим по выборке строк
        for string in sliceOfStrings:

            # Определяем медианное значение в каждой строке и добавляем в cписок элемент (значениеб строка)
            stringsWithMediansList.append(
                (getMedianOfStringByASCII(string), string))

        # Сортируем список по первому значению каждого элемента, т.е. по медианному
        sortedList = sorted(stringsWithMediansList, reverse=False)

        # В первом элементе отсортированного списка находится медианное значение с самым низким значением и строка
        # Помещаем ее в итоговый выходной список
        outputStringsList.append(sortedList[0][1])

    outputString = "\n".join(outputStringsList)

    print("Результат работы:")
    print("")

    print("Исходная строка: ")
    print("")
    print(inputString)
    print("")
    print("Отсортированная строка: ")
    print("")
    print(outputString)

    return

#
# Задача 8.  порядке увеличения квадратичного отклонения между средним весом ASCII-кода символа в строке и максимально среднего ASCII-кода
# тройки подряд идущих символов в строке.
#


# Вычисления квадратичного отклонения между средним весом ASCII-кода символа в строке и
# максимально среднего ASCII-кода тройки подряд идущих символов в строке.


def squareDeviation(string):

    asciiCodes = []

    # Проходим по символам строки
    for char in string:

        # Определяем ASCII код символа
        asciiCode = ord(char)

        # Добавляем к списку
        asciiCodes.append(asciiCode)

    # Вычисление среднего значения ASCII-кодов
    averageASCIICodes = sum(asciiCodes) / len(asciiCodes)

    # Список средних значений для троек символов
    averageTriplets = []

    # Вычисление среднего значения для каждой тройки символов
    for index in range(len(asciiCodes) - 3):
        oneItem = asciiCodes[index]
        twoItem = asciiCodes[index + 2]
        treeItem = asciiCodes[index + 3]
        averageTriplets.append((oneItem + twoItem + treeItem) / 3)

    # # Вычисление максимального среднего значения для троек символов
    maxAverageTriplet = max(averageTriplets)

    # Квадратичне отклонение
    squareDeviation = (averageASCIICodes - maxAverageTriplet) ** 2

    return squareDeviation


def sortStringsBySquareDeviation(inputString):

    # Разбиваем строки по символу новой строки - \n
    stringsList = inputString.split("\n")

    stringWithDeviationList = []

    for string in stringsList:

        deviation = squareDeviation(string)

        stringWithDeviationList.append((deviation, string))

    # Сортируем список по первому значению каждого элемента, т.е. по квадратичному отклонению
    sortedList = sorted(stringWithDeviationList, reverse=False)

    outputString = "\n".join(string
                             for (_, string) in sortedList)

    print("Результат работы:")
    print("")

    print("Исходная строка: ")
    print("")
    print(inputString)
    print("")
    print("Отсортированная строка: ")
    print("")
    print(outputString)

    return


#
# Задача 11.  В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального
# среднего веса ASCII-кода тройки символов в первой строке.
#

#
# Вычисление максимального среднего веса ASCII-кода тройки символов в строке
#

def maxAvrWeight(string: str):

    # Список средних весов ASCII кодов троек символов
    avrWeights = []

    for index in range(0, len(string)-2, 3):

        # Вычисление ASCII кодов первого, второго, третьего символа стройки
        charOne = ord(string[index])
        charTwo = ord(string[index + 1])
        charTree = ord(string[index + 2])

        # Вычисление среднего веса ASCII кодов тройки символов
        avr = (charOne + charTwo + charTree)/3

        # Добавлление в список
        avrWeights.append(avr)

    # Вычисление максимального значения среднего веса ASCII кодов тройки символов в списке
    maxAvrWeightByAll = max(avrWeights)

    return maxAvrWeightByAll

#
# Вычисление квадратичного отклонения дисперсии двух чисел
#


def squareDeviation2(num1: float, num2: float):

    # Вычисление среднего значения
    avg = (num1 + num2) / 2

    # Вычисление суммы квадратов отклонений от среднего значения
    sumSquares = ((num1 - avg) ** 2 + (num2 - avg) ** 2)

    # Вычисление дисперсии
    dispersion = sumSquares / 2

    # Вычисление квадратичного отклонения
    squareDeviationByDispersion = dispersion ** 0.5

    return squareDeviationByDispersion


def sortStringsBySquareDeviation2(inputString: str):

    # Разбиваем строки по символу новой строки - \n
    stringsList = inputString.split("\n")

    # Максимальный средний вес ASCII-кода тройки символов в ПЕРВОЙ строке
    maxAvrWeightFirstString = maxAvrWeight(stringsList[0])

    # Список, элементы которого будут содержать (квадратичного отклонения дисперсииб саму строку)
    stringsWithSquareDeviationList = []

    for string in stringsList:
        maxAvrWeightString = maxAvrWeight(string)
        squareDeviationString = squareDeviation2(
            maxAvrWeightString, maxAvrWeightFirstString)

        stringsWithSquareDeviationList.append((squareDeviationString, string))

    # Сортируем список по первому значению каждого элемента, т.е. по квадратичному отклонению
    sortedList = sorted(stringsWithSquareDeviationList, reverse=False)

    outputString = "\n".join(string
                             for (_, string) in sortedList)

    print("Результат работы:")
    print("")

    print("Исходная строка: ")
    print("")
    print(inputString)
    print("")
    print("Отсортированная строка: ")
    print("")
    print(outputString)

    return


userInput = ""

while userInput.lower() != "exit":

    print("")
    print("1. Отсортировать строки в указанном порядке: В порядке увеличения среднего веса ASCII-кода символа строки.")
    print("2. Отсортировать строки в указанном порядке: В порядке увеличения медианного значения выборки строк (прошлое медианное значение удаляется из выборки и производится поиск нового медианного значения).")
    print("3. Отсортировать строки в указанном порядке: В порядке увеличения квадратичного отклонения между средним весом ASCII-кода символа в строке и максимально среднего ASCII-кода тройки подряд идущих символов в строке.")
    print("4. Отсортировать строки в указанном порядке: В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.")
    print("")
    userInput = input("Введите номер задачи или exit: ")
    print("")

    if userInput == "1":
        averageWeightSymbols(inputStringForTasks)
    elif userInput == "2":
        stringsMedian(inputStringForTasks)
    elif userInput == "3":
        sortStringsBySquareDeviation(inputStringForTasks)
    elif userInput == "4":
        sortStringsBySquareDeviation2(inputStringForTasks)
