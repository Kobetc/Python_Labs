import random

inputString = "Дана строка. Необходимо перемешать все символы строки в случайном порядке."

# Задача 5. Дана строка. Необходимо перемешать все символы строки в случайном порядке.


def randomizeString(inputString):

    # Входную строку преобразовываем в список
    outputList = list(inputString)

    # Возвращаем НОВЫЙ перемешанный список
    randomizedOutputList = random.sample(
        outputList, len(outputList))

    # Сливаем список в строку
    outputString = ("").join(randomizedOutputList)

    # "Дана строка. Необходимо перемешать все символы строки в случайном порядке."
    print(inputString)
    # " оНс твебв.лаотедсшемвнеыуоосок то  аооерркпя симарймди  Ди. льаепнкчхсрам"
    print(outputString)

    return outputString


randomizeString(inputString)
