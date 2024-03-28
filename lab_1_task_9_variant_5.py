#
# Задание 9. Прочитать список строк с клавиатуры. Упорядочить по длине строки.
#

userInput = ""
inputStringList = []

while userInput.lower() != "exit":
    userInput = input("Введите строку или exit: ")
    inputStringList.append(userInput)

# Проходим по списку строк и формируем новый список из элементов (длина строки, строка)
# Сортируем полученный список по первому значению элементов списка, т.е. по длине
sortedStringList = sorted(((len(string), string)
                          for string in inputStringList), reverse=False)

# Проходим по отсортированному списку и создаем новый список только из строк, отсеивая длину строки
# Сливаем полученный список строк в строку, вставляя между элементами символ новой строки \n
outputString = "\n".join(string
                         for (len, string) in sortedStringList)

print(outputString)
