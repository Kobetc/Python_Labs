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

    print("Результат работы:")
    print("")
    # "Дана строка. Необходимо перемешать все символы строки в случайном порядке."
    print("Исходная строка: ", inputString)
    # " оНс твебв.лаотедсшемвнеыуоосок то  аооерркпя симарймди  Ди. льаепнкчхсрам"
    print("Перемешанная строка: ", outputString)

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

    print("Результат работы:")
    print("")

    # ['P', 'T', 'N', 'T', 'P']
    print("Исходный набор заглавных букв: ", capitalLettersList)

    # ['P', 'T', 'N', 'T', 'P']
    print("Перевернутый набор заглавных букв: ",  invertedCapitalLettersList)

    # True
    print("Равны ли наборы: ",  capitalLettersList == invertedCapitalLettersList)

    # Сравниваем прямой и перевернутый список. Если списки равны, значит прописные символы этой строки образуют палиндром
    return capitalLettersList == invertedCapitalLettersList

#
# Задача 14. Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.
#


def sortString(inputString: str):

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

    print("Результат работы:")
    print("")
    # Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.
    print("Исходная строка: ", inputString)
    # в по Дана букв слова слове через каждом пробел строка которой записаны Необходимо количеству упорядочить
    print("Упорядоченная строка: ", outputString)

    return outputString


userInput = ""

while userInput.lower() != "exit":

    print("")
    print("1. Дана строка. Необходимо перемешать все символы строки в случайном порядке.")
    print("2. Дана строка, состоящая из символов латиницы. Необходимо проверить, образуют ли прописные символы этой строки палиндром.")
    print("3. Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.")
    print("")
    userInput = input("Введите номер задачи или exit: ")
    print("")

    if userInput == "1":
        randomizeString(inputStringForTask5)
    elif userInput == "2":
        checkCapitalLetters(inputStringForTask7)
    elif userInput == "3":
        sortString(inputStringForTask14)
