import random

inputStringForTask5 = "Дана строка. Необходимо перемешать все символы строки в случайном порядке."
inputStringForTask7 = "Pdfgd, fghgT: fghfghNfghfgh. Tfgdfgd Pdhfgh"
inputStringForTask14 = "Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове."

#
# Задача 5. Дана строка. Необходимо перемешать все символы строки в случайном порядке.
#


def randomizeString(inputString):

    # Входную строку преобразовываем в список по словам символам
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

#
# Задача 14. Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.
#


def randomizeString(inputString: str):

    # Входную строку преобразовываем в список по словам, удаляя предварительно из строки запятые и точки, если они есть
    wordList = inputString.replace(".", "").replace(",", "").split(" ")

    # Словарь, в котором ключами будут слова, а значениями их длина
    wordDictionary = {}

    # Каждое слово помещаем в словарь в каачестве ключа, в качестве значения - его длина
    for word in wordList:
        wordDictionary[word] = len(word)

    # Сортируем словарь по значениям, по возрастанию, reverse=False. По убыванию - reverse=True.
    # Получаем список элементов (значение, ключ). Сортировка по первому элементу, т.е. value. В котором у нас длина слова.
    sortedWordList = sorted(((value, key)
                             for (key, value) in wordDictionary.items()), reverse=False)

    outputWordList = []

    for (value, key) in sortedWordList:
        outputWordList.append(key)

    outputString = " ".join(outputWordList)

    # Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.
    print(inputString)
    # в по Дана букв слова слове через каждом пробел строка которой записаны Необходимо количеству упорядочить
    print(outputString)

    return outputString


randomizeString(inputStringForTask5)

checkCapitalLetters(inputStringForTask7)

randomizeString(inputStringForTask14)
