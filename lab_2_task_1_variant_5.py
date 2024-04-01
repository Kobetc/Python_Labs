
#
# Задача 1. Кубики.
#

import random


def colorsKubes():

    # Набор цветов у игрока Аня
    colorArrayA = []

    # Набор цветов у игрока Боря
    colorArrayB = []

    # Набор общих цветов обоих игроков
    summArray = set()

    # Набор цветов только игрока Аня
    onlyAArray = set()

    # Набор цветов только игрока Боря
    onlyBArray = set()

    # Вводим число цветов у игрока Аня и Боря
    colorNumberA = int(input("Число цветов Ани: "))
    colorNumberB = int(input("Число цветов Бори: "))

    # Заполняем список с цветами игрока Аня, случайными номерами цвета от 0 до 10 ** 8
    for _ in range(0, colorNumberA):
        colorArrayA.append(random.randrange(0, 10**8 + 1))

    # Заполняем список с цветами игрока Боря, случайными номерами цвета от 0 до 10 ** 8
    for _ in range(0, colorNumberB):
        colorArrayB.append(random.randrange(0, 10**8 + 1))

    # Проходим по цветам игрока Аня
    for colorNumber in colorArrayA:

        # Если цвет Ани находится и в списке цветов Бори
        if colorNumber in colorArrayB:

            # Добавляем в словарь с ОБЩИМИ цветами номер цвета
            summArray.add(colorNumber)
        else:
            # Иначе, добавляем цвет в список цветов ТОЛЬКО Ани
            onlyAArray.add(colorNumber)

    # Проходим по цветам игрока Бори
    for colorNumber in colorArrayB:

        # Если цвет Бори находится и в списке цветов Бори
        if colorNumber in colorArrayA:

            # Добавляем в словарь с ОБЩИМИ цветами номер цвета
            summArray.add(colorNumber)

        else:
            # Иначе, добавляем цвет в список цветов ТОЛЬКО Бори
            onlyBArray.add(colorNumber)

    print("Результат работы:")
    print("")

    print("Введенное число цветов игрока Ани: ", colorNumberA)
    print("Введенное число цветов игрока Бори: ", colorNumberB)
    print("Цвет  игрока Ани: ", colorArrayA)
    print("Цвета игрока Бори: ", colorArrayB)

    print("Число общих цветов двух игроков: ", len(summArray))
    print("Общие цвета двух игроков: ",  summArray)

    print("Число цветов ТОЛЬКО игрока Аня: ", len(onlyAArray))
    print("Цвета ТОЛЬКО игрока Аня: ",  onlyAArray)

    print("Число цветов ТОЛЬКО игрока Боря: ", len(onlyBArray))
    print("Цвета ТОЛЬКО игрока Боря: ",  onlyBArray)


colorsKubes()
