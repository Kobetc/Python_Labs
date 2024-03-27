
# Список, содержащий все русские буквы
import sys


cyrillicSymbolList = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
numberSymbolList = list('0123456789')

inputStringForTask5 = "Д45ана стfdgрока. Необходимо найти, наибоdfgльшее к5656ghоличество идуkjhkщих под87kряд сим87kkволов. кир7k8tkиллицы."
inputStringForTask7 = "Натуральные числа  — числа, возникающие естественным образом при счёте ( 1.0. 1,0, 1, 15, 25, 35, 45, 55, 65, 75 ... 100 ... 1000 и так далее )."
inputStringForTask14 = "Например: -1234325.435874358729, 1.0. 1,0, 1, 15, 25, 35, 45, 55, 65, 75 ... 100 ... 1000 ... 12345.232."

#
# Задача 5. Дана строка. Необходимо найти наибольшее количество идущих подряд символов кириллицы.
#


def maxLenCyrillic(inputString):

    maxLen = 0                      # Максимальная длина кирилитической последовательности
    # Индекс начала максимальной кирилитической последовательности
    indexStartMaxLenCyrillic = 0

    startCyrillic = False           # Признак начала кирилитической последовательности
    currentCyrilicLen = 0           # Текущая длина кирилитической последовательности
    # Текущий индекс начала кирилитической последовательности
    currentIndexStartCyrillic = 0

    # Перебираем все индексы символов в заданной строке
    for charIndex in range(len(inputString)):

        # Если в строке по текущему индекссу символ находится в списке, содержащий все русские буквы
        if inputString[charIndex].lower() in cyrillicSymbolList:

            # Если до этого момента шли не кирилитические символы
            if startCyrillic == False:

                # Выставляем признак начала кирилитической последовательности
                startCyrillic = True

                # Текущая длина кирилитической последовательности = 1
                currentCyrilicLen = 1

                # Индекс начала последовательности = текущему индексу
                currentIndexStartCyrillic = charIndex
            else:

                # Иначе, уже не первый кирилитический символ и увеличиваем длину последовательности
                currentCyrilicLen = currentCyrilicLen + 1
        else:
            # Символ не относиться к кирилице. Предполагаем, что только что закончилась
            # кирилитическая последовательность.
            # Если текущая длина последовательности больше текущей максимальной,
            # то сохраняем ее как максимальную длину последовательности и индекс ее начала
            if currentCyrilicLen > maxLen:
                maxLen = currentCyrilicLen
                indexStartMaxLenCyrillic = currentIndexStartCyrillic

            # Сбрасываем значения текущей длины, индекса и признак начала кирилитической последовательности
            startCyrillic = False
            currentCyrilicLen = 0
            currentIndexStartCyrillic = 0

    print("Результат работы:")
    print("")
    # Д45ана стfdgрока. Необходимо найти, наибоdfgльшее к5656ghоличество идуkjhkщих под87kряд сим87kkволов. кир7k8tkиллицы.
    print("Исходная строка: ", inputString)
    # 10 18
    print("Максимальная длина последовательности кирилицы и ее начальный индекс в строке: ",
          maxLen, indexStartMaxLenCyrillic)
    # Необходимо
    print("Максимальная последовательность кирилицы: ",
          inputString[indexStartMaxLenCyrillic:indexStartMaxLenCyrillic+maxLen])

    return


#
# Задача 7. Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.
#

def minNaturNumber(inputString):

    # Начальное значение минимального числа - максимальное допустимое число в системе
    minNumber = sys.maxsize

    # Входную строку преобразовываем в список по словам
    wordList = inputString.split(" ")

    # Перебираем слова в строке
    for word in wordList:

        # Очищаем слово от точки или запятой, если они есть в конце слова
        clearedWord = word.rstrip(",.")

        try:
            # Пробуем преобразовать слово в целове число. Если преобразование не вызвало исключение,
            # значит слово является числом
            digit = int(clearedWord)

            # Проверяем, что число изначально было целым. Отсеиваются дробные числа. И проверяем, что число больше 0
            if str(digit) == clearedWord and digit > 0:

                # Если число меньше ранее сохраненного, то оно является минимальным на текущий момент
                if digit < minNumber:
                    minNumber = digit

        except:
            # Если слово не содержало число и int(clearedWord) вызвал исключение, пропускаем данное слово
            pass

    print("Результат работы:")
    print("")
    # Д45ана стfdgрока. Необходимо найти, наибоdfgльшее к5656ghоличество идуkjhkщих под87kряд сим87kkволов. кир7k8tkиллицы.
    print("Исходная строка: ", inputString)
    # 10 18
    print("Минимальное из имеющихся в исходной строке натуральных чисел: ", minNumber)

    return

#
# Задача 14. Дана строка. Необходимо найти наибольшее количество идущих подряд цифр.
#


def maxLenNumber(inputString: str):

    maxLen = 0                      # Максимальная длина цифровой последовательности

    # Индекс начала максимальной цифровой последовательности
    indexStartMaxLenNumbers = 0

    startNumbers = False           # Признак начала цифровой последовательности
    currentNumbersLen = 0           # Текущая длина v
    # Текущий индекс начала цифровой последовательности
    currentIndexStartNumbers = 0

    # Перебираем все индексы символов в заданной строке
    for charIndex in range(len(inputString)):

        # Если в строке по текущему индекссу символ находится в списке, содержащий все числа
        if inputString[charIndex].lower() in numberSymbolList:

            # Если до этого момента шли не цифровые символы
            if startNumbers == False:

                # Выставляем признак начала цифровой последовательности
                startNumbers = True

                # Текущая длина цифровой последовательности = 1
                currentNumbersLen = 1

                # Индекс начала цифровой последовательности = текущему индексу
                currentIndexStartNumbers = charIndex
            else:

                # Иначе, уже не первый цифровой символ и увеличиваем длину цифровой последовательности
                currentNumbersLen = currentNumbersLen + 1
        else:
            # Символ не относиться к цифре. Предполагаем, что только что закончилась
            # цифровой последовательности.
            # Если текущая длина последовательности больше текущей максимальной,
            # то сохраняем ее как максимальную длину последовательности и индекс ее начала
            if currentNumbersLen > maxLen:
                maxLen = currentNumbersLen
                indexStartMaxLenNumbers = currentIndexStartNumbers

            # Сбрасываем значения текущей длины, индекса и признак начала цифровой последовательности
            startNumbers = False
            currentNumbersLen = 0
            currentIndexStartNumbers = 0

    print("Результат работы:")
    print("")
    # Например: -1234325.435874358729, 1.0. 1,0, 1, 15, 25, 35, 45, 55, 65, 75 ... 100 ... 1000 ... 12345.232.
    print("Исходная строка: ", inputString)
    # 12 19
    print("Максимальная длина цифровой последовательности и ее начальный индекс в строке: ",
          maxLen, indexStartMaxLenNumbers)
    # 435874358729
    print("Максимальная цифровая последовательность: ",
          inputString[indexStartMaxLenNumbers:indexStartMaxLenNumbers+maxLen])

    return


userInput = ""

while userInput.lower() != "exit":

    print("")
    print("1. Дана строка. Необходимо найти наибольшее количество идущих подряд символов кириллицы.")
    print("2. Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.")
    print("3. Дана строка. Необходимо найти наибольшее количество идущих подряд цифр.")
    print("")
    userInput = input("Введите номер задачи или exit: ")
    print("")

    if userInput == "1":
        maxLenCyrillic(inputStringForTask5)
    elif userInput == "2":
        minNaturNumber(inputStringForTask7)
    elif userInput == "3":
        maxLenNumber(inputStringForTask14)
