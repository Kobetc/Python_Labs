

import random


digitalArrayForTask5 = [random.randrange(
    0, 100) for index in range(random.randrange(10, 30))]
indexForTask5 = random.randrange(0, len(digitalArrayForTask5))


#
# Задача 5. Дан целочисленный массив и натуральный индекс (число, меньшее
# размера массива). Необходимо определить является ли элемент по указанному индексу глобальным минимумом.
#


def isMinByIndex(digitalArray: list, index: int):

    # Определение минимального значения в числовом списке
    minValueInList = min(digitalArray)

    # Определение значение в списке по заданному индексу
    valueFromListByIndex = digitalArray[index]

    # Являются ли эти значениея одинаковыми, если True, то элемент по указанному индексу является глобальным минимумом
    isMinByIndex = minValueInList == valueFromListByIndex

    print(digitalArray, index, minValueInList,
          valueFromListByIndex, isMinByIndex)

    # Целочисленный массив:  [63, 36, 93, 29, 87, 42, 32, 24, 24, 30, 80, 82, 41, 84, 93, 15, 8, 87, 6, 20, 79]
    # Натуральный индекс:  18
    # Минимальное число в массиве:  6 минимальное число по заданному индексу:  6
    # Является ли элемент по указанному индексу глобальным минимумом:  True

    print("Результат работы:")
    print("")
    # Целочисленный массив
    print("Целочисленный массив: ", digitalArray)
    # Натуральный индекс
    print("Натуральный индекс: ", index)
    print("Минимальное число в массиве: ", minValueInList,
          "минимальное число по заданному индексу: ", valueFromListByIndex)
    print("Является ли элемент по указанному индексу глобальным минимумом: ", isMinByIndex)

    return


isMinByIndex(digitalArrayForTask5, indexForTask5)
