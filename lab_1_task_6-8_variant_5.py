
cyrillicSymbolList = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

inputStringForTask5 = "Д45ана стfdgрока. Необходимо найти, наибоdfgльшее к5656ghоличество идуkjhkщих под87kряд сим87kkволов. кир7k8tkиллицы."


#
# Задача 5. Дана строка. Необходимо найти наибольшее количество идущих подряд символов кириллицы.
#

def maxLenCyrillic(inputString: str):

    maxLen = 0
    indexStartMaxLenCyrillic = 0

    startCyrillic = False
    currentCyrilicLen = 0
    currentIndexStartCyrillic = 0

    for charIndex in range(len(inputString)):
        if inputString[charIndex].lower() in cyrillicSymbolList:
            if startCyrillic == False:

                startCyrillic = True
                currentCyrilicLen = 1
                currentIndexStartCyrillic = charIndex
            else:
                currentCyrilicLen = currentCyrilicLen + 1
        else:

            if currentCyrilicLen > maxLen:
                maxLen = currentCyrilicLen
                indexStartMaxLenCyrillic = currentIndexStartCyrillic

            startCyrillic = False
            currentCyrilicLen = 0
            currentIndexStartCyrillic = len(inputString)

    print("Результат работы:")
    print("")
    # Д45ана стfdgрока. Необходимо найти, наибоdfgльшее к5656ghоличество идуkjhkщих под87kряд сим87kkволов. кир7k8tkиллицы.
    print("Исходная строка: ", inputStringForTask5)
    # 10 18
    print("Максимальная длина последовательности кирилицы и ее начальный индекс в строке: ",
          maxLen, indexStartMaxLenCyrillic)
    print("Максимальная последовательность кирилицы: ",
          inputStringForTask5[indexStartMaxLenCyrillic:indexStartMaxLenCyrillic+maxLen])

    return


maxLenCyrillic(inputStringForTask5)
