
# Список, содержащий все русские буквы
import sys


cyrillicSymbolList = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

inputStringForTask5 = "Д45ана стfdgрока. Необходимо найти, наибоdfgльшее к5656ghоличество идуkjhkщих под87kряд сим87kkволов. кир7k8tkиллицы."
inputStringForTask7 = "Натуральные числа  — числа, возникающие естественным образом при счёте ( 1.0. 1,0, 1, 15, 25, 35, 45, 55, 65, 75 ... 100 ... 1000 и так далее )."

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
    print("Максимальная последовательность кирилицы: ",
          inputStringForTask5[indexStartMaxLenCyrillic:indexStartMaxLenCyrillic+maxLen])

    return


#
# Задача 7. Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.
#

def minNaturNumber(inputString: str):

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


maxLenCyrillic(inputStringForTask5)

minNaturNumber(inputStringForTask7)
