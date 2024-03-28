

import random


digitalArrayForTask5_17 = [random.randrange(
    0, 10) for index in range(random.randrange(10, 20))]
indexForTask5 = random.randrange(0, len(digitalArrayForTask5_17))


#
# Задача 5. Дан целочисленный массив и натуральный индекс (число, меньшее
# размера массива). Необходимо определить является ли элемент по указанному индексу глобальным минимумом.
#


def isMinByIndex(digitalArray, index):

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

#
# Задача 17. Дан целочисленный массив. Необходимо поменять местами минимальный и максимальный элементы массива.
#


def exchangeMinMax(digitalArray: list):

    # Создаем копию числового массива
    copyDigitalArray = digitalArray.copy()

    # Определяем минимальное число в массиве
    minValueInArray = min(copyDigitalArray)
    # Определяем индекс в массиве найденного минимального числа. Первое вхождение.
    firstIndexMinValue = copyDigitalArray.index(minValueInArray)

    # Определяем максимальное число в массиве
    maxValueInArray = max(copyDigitalArray)
    # Определяем индекс в массиве найденного максимального числа. Первое вхождение.
    firstIndexMaxValue = copyDigitalArray.index(maxValueInArray)

    # По индексу минимального числа записываем максимальное число
    copyDigitalArray[firstIndexMinValue] = maxValueInArray
    # По индексу максимального числа записываем минимальное число
    copyDigitalArray[firstIndexMaxValue] = minValueInArray

    print("Результат работы:")
    print("")
    # Целочисленный массив
    print("Целочисленный массив: ", digitalArray)
    print("Минимальное число в массиве: ", minValueInArray,
          "его первый индекс: ", firstIndexMinValue)
    print("Максимальное число в массиве: ", maxValueInArray,
          "его первый индекс: ", firstIndexMaxValue)
    print("Целочисленный массив с замененными минимальным и максимальным элементами массива: ",
          copyDigitalArray)

    return


isMinByIndex(digitalArrayForTask5_17, indexForTask5)

exchangeMinMax(digitalArrayForTask5_17)
