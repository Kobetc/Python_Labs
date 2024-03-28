

import random


digitalArrayForTask5_17_29 = [random.randrange(
    0, 100) for index in range(random.randrange(10, 40))]
indexForTask5 = random.randrange(0, len(digitalArrayForTask5_17_29))
indexRangeForTask29 = [random.randrange(0, (len(digitalArrayForTask5_17_29) // 2)),
                       random.randrange((len(digitalArrayForTask5_17_29) // 2), len(digitalArrayForTask5_17_29))]


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

#
# Задача 29. Дан целочисленный массив и интервал a..b. Необходимо проверить наличие максимального элемента массива в этом интервале.
#


def findMaxInRange(digitalArray: list, indexRange: list):

    # Определяем максимальное число в массиве
    maxValueInArray = max(digitalArray)
    # Определяем индекс в массиве найденного максимального числа. Первое вхождение.
    firstIndexMaxValue = digitalArray.index(maxValueInArray)

    # Проверяем, находится ли максимальное значение массива в срезе этого массива ограниченного
    # индексами из интервала
    isMaxValueInRange = maxValueInArray in digitalArray[indexRange[0]:indexRange[1]]

    print("Результат работы:")
    print("")
    # Целочисленный массив
    print("Целочисленный массив: ", digitalArray)
    print("Интервал с индексами начала:",
          indexRange[0], "конца: ", indexRange[1])
    print("Максимальное значение в массиве: ",
          maxValueInArray, "его индекс: ", firstIndexMaxValue)
    print("Находится ли максимальное значение в интервале: ", isMaxValueInRange)

    return


isMinByIndex(digitalArrayForTask5_17_29, indexForTask5)

exchangeMinMax(digitalArrayForTask5_17_29)

findMaxInRange(digitalArrayForTask5_17_29, indexRangeForTask29)
