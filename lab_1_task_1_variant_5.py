import math

#
# Задача 1. Найти количество делителей числа, не делящихся на 3.
#


def noDivToTree():

    # Число делителей, не делящихся на 3
    countDividersNotThree = 0

    # Список делителей, не делящихся на 3
    dividersNotThreeList = []

    # Вводим число
    inputedNumber = int(input("Введите число: "))

    # Перебираем все числа от 1 до введенное число деленное на 2 + 1
    for divider in range(1, inputedNumber // 2 + 1):

        # Если число разделилось на на цело - значит это делитель
        if inputedNumber % divider == 0:

            # Если дклитель разделился на 3 с остатком, значит это искомый делитель
            if divider % 3 != 0:

                # Увеличиваем счетчик делителей
                countDividersNotThree += 1

                # Добавляем найденный делитель в список
                dividersNotThreeList.append(divider)

    print("Результат работы:")
    print("")

    print("Введенное число : ", inputedNumber)
    print("Число делителей введенного числачисла, не делящихся на 3: ",
          countDividersNotThree)
    print("Делители введенного числачисла, не делящихся на 3: ",
          dividersNotThreeList)

#
# Задача 2. Найти минимальную нечетную цифру числа.
#


def minDigitOfNumber():

    # Минимальная цифра числа. Инициализируем числом, заведомо большим, чем максимально возможная цифра.
    minNumber = 10

    # Вводим число в виде строки
    inputedNumber = input("Введите число: ")

    # Проходим по всем символам числа
    for digitSymbol in inputedNumber:

        # Переводим символ в число и сравниваем с текущим минимальным числом. Если оно меньше, значит это новая минимальная цифра в числе
        if int(digitSymbol) < minNumber:

            #  Если цифра не делится на 2 без остатка
            if int(digitSymbol) % 2 != 0:

                # Значит это новая искомая минимальная цифра числа, не четная
                minNumber = int(digitSymbol)

    print("Результат работы:")
    print("")

    print("Введенное число : ", inputedNumber)
    print("Минимальная нечетная цифра числа: ",
          minNumber)


#
# Задача 3. Найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа.
#

def summAllDivs():

    # Список делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа
    dividersList = []

    # Сумма делителей числа
    dividerSumm = 0

    # Сумма цифр числа
    digitalSumm = 0

    # Произведение цифр числа
    digitalMulty = 1

    # Вводим число в виде строки
    inputedNumberStr = input("Введите число: ")

    # Преобразуем строку в число
    inputedNumberDigtal = int(inputedNumberStr)

    # Для каждого символа числа преобразуем его в число, суммируем и умножаем с предыдущей суммой и произведением
    for digitSymbol in inputedNumberStr:
        digitalSumm = digitalSumm + int(digitSymbol)
        digitalMulty = digitalMulty * int(digitSymbol)

    # Перебираем все числа от 1 до введенное число деленное на 2 + 1
    for divider in range(1, inputedNumberDigtal // 2 + 1):

        # Если число разделилось на на цело - значит это делитель
        if inputedNumberDigtal % divider == 0:

            # Если НОД найденного делителя и суммы цифр числа равен 1, значит они взаимопростые
            # Если НОД найденного делителя и произведения цифр числа не равен 1, значит они не взаимопростые
            # Если оба эти условия выполняются, найден нужный делитель и он ссумируется с предыдущими
            if math.gcd(digitalSumm, divider) == 1 and math.gcd(digitalMulty, divider) != 1:
                dividerSumm = dividerSumm + divider
                dividersList.append(divider)

    print("Результат работы:")
    print("")

    print("Введенное число : ", inputedNumberStr)
    print("Сумма цифр веденного числа : ", digitalSumm)
    print("Произведение цифр веденного числа : ", digitalMulty)
    print("Сумма всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа: ",
          dividerSumm)
    print("Делители числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа: ",
          dividersList)


userInput = ""

while userInput.lower() != "exit":

    print("")
    print("1. Найти количество делителей числа, не делящихся на 3.")
    print("2. Найти минимальную нечетную цифру числа.")
    print("3. Найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа.")
    print("")
    userInput = input("Введите номер задачи или exit: ")
    print("")

    if userInput == "1":
        noDivToTree()
    elif userInput == "2":
        minDigitOfNumber()
    elif userInput == "3":
        summAllDivs()
