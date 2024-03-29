
# Число фийлов
filesNumber = 0

# Словарь. В качестве ключей - имя файла, в качестве значения - список с символами типа доступа r, w, x
files = {}

userInput = ""

# Вводим число файлов
try:
    filesNumber = int(input("Введите число файлов: "))
except:
    print("Введите число !")

# Создаем цикл по числу файлов
for _ in range(filesNumber):

    # Запрашиваем имя файла и символы доступа к ним, через пробелы
    fileWithAccess = input("Введите имя файла и доступы к ним (r, w, x): ")

    # Разбиваем строку введенную пользователем на список по пробелам
    fileWithAccessArray = fileWithAccess.split(" ")
    try:

        # Первый элемент списка должен содержать имя файла
        fileName = fileWithAccessArray[0].lower()

        # Остальная часть списка, от второго и до конца - символы доступа к файлу
        fileAccesses = fileWithAccessArray[1:]

        # Проверяем, что пользователь ввел верные символы доступа к файлу, иначе, выходим из программы
        for access in fileAccesses:
            if access.lower() not in ["w", "r", "x"]:
                userInput = "exit"
                break

        # Добавляем в словарь новый элемент. С ключем - имя файла, значение - список с символами доступа
        files[fileName] = fileAccesses
    except:
        print("Введите имя файла и доступы к ним через пробелы !")

print(files)

# Бесконечный цикл, пока пользователь не введет exit
while userInput.lower() != "exit":

    # Запрашиваем у пользователя имя операции с файлом и имя файла. Через пробел
    userInput = input(
        "Введите операцию (read, write, execute) и имя файла из списка или exit:")

    # Разбиваем введенную строку в список по пробелам
    userInputArray = userInput.split(" ")

    operation = ""
    file = ""

    # Первый элемент списка должен содержать операция с файлом
    # Второй элемент - имя файла
    try:
        operation = userInputArray[0].lower()
        file = userInputArray[1].lower()
    except:
        print("Введите операцию и имя файла через пробелы !")

    # Проверяем, что имя операции введенно верно, является одним из списка ["read", "write", "execute"]
    if operation.lower() in ["read", "write", "execute"]:

        # Проверяем, что имя файла соответствует одному из ключей в словаре файлов.
        if file in files:

            # Если имя операции одно из "read", "write", "execute"
            match operation.lower():
                case "read":
                    # Проверяем, есть ли символ "r" в списке значений по ключу, имя файла, в словаре
                    # Если да, то выводим OK, иначе - Access denied
                    print("OK") if "r" in files[file] else print(
                        "Access denied")
                case "write":
                    # Проверяем, есть ли символ "w" в списке значений по ключу, имя файла, в словаре
                    # Если да, то выводим OK, иначе - Access denied
                    print("OK") if "w" in files[file] else print(
                        "Access denied")
                case "execute":
                    # Проверяем, есть ли символ "x" в списке значений по ключу, имя файла, в словаре
                    # Если да, то выводим OK, иначе - Access denied
                    print("OK") if "x" in files[file] else print(
                        "Access denied")
