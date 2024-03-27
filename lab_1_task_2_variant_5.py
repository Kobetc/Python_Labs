import random

inputStringForTask5 = "Дана строка. Необходимо перемешать все символы строки в случайном порядке."
inputStringForTask7 = "Pdfgd, fghgT: fghfghNfghfgh. Tfgdfgd Pdhfgh"

#
# Задача 5. Дана строка. Необходимо перемешать все символы строки в случайном порядке.
#


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

#
# Задача 7. Дана строка, состоящая из символов латиницы. Необходимо проверить, образуют ли прописные символы этой строки палиндром.
#


def checkCapitalLetters(inputString):

    # Список для заглавных букв
    capitalLettersList = []

    # Перевернутый список для заглавных букв
    invertedCapitalLettersList = []

    # Проходим по каждому символу строки
    for char in inputString:

        # Если символ является заглавной буквой
        if char.isupper():

            # Добавляем символ в список
            capitalLettersList.append(char)

    # Переворачиваем список заглавных букв, делая срез от начало до конца с шагом -1
    invertedCapitalLettersList = capitalLettersList[::-1]

    print(capitalLettersList, invertedCapitalLettersList,
          capitalLettersList == invertedCapitalLettersList)  # ['P', 'T', 'N', 'T', 'P'] ['P', 'T', 'N', 'T', 'P']

    # Сравниваем прямой и перевернутый список. Если списки равны, значит прописные символы этой строки образуют палиндром
    return capitalLettersList == invertedCapitalLettersList


randomizeString(inputStringForTask5)

checkCapitalLetters(inputStringForTask7)
