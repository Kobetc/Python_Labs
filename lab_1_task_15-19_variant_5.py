

import random


digitalArrayForTask5_17_29_41_53 = [random.randrange(
    -10, 10) for _ in range(random.randrange(10, 40))]
indexForTask5 = random.randrange(0, len(digitalArrayForTask5_17_29_41_53))
indexRangeForTask29 = [random.randrange(0, (len(digitalArrayForTask5_17_29_41_53) // 2)),
                       random.randrange((len(digitalArrayForTask5_17_29_41_53) // 2), len(digitalArrayForTask5_17_29_41_53))]


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


def exchangeMinMax(digitalArray):

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


def findMaxInRange(digitalArray, indexRange):

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

#
# Задача 41. Дан целочисленный массив. Найти среднее арифметическое модулей его элементов.
#


def averageModules(digitalArray: list):

    # Сумма всех значений элементов списка
    sumDigits = 0

    # Проходим по всем элементам списка и суммируем их после приведения по модулю
    for digit in digitalArray:
        sumDigits = sumDigits + abs(digit)

    # Вычисляем среднее значение, сумму элементов списка делим на длину списка
    averageDigits = sumDigits / len(digitalArray)

    print("Результат работы:")
    print("")
    # Целочисленный массив
    print("Целочисленный массив: ", digitalArray)
    print("Среднее арифметическое модулей эдементов массива:", averageDigits)

    return

#
# Задача 53. Для введенного списка построить новый с элементами, большими,
# чем среднее арифметическое списка, но меньшими, чем его максимальное значение.
#


def newList(digitalArray: list):

    # Сумма всех значений элементов списка
    sumDigits = 0

    # Проходим по всем элементам списка и суммируем их
    for digit in digitalArray:
        sumDigits = sumDigits + digit

    # Вычисляем среднее значение, сумму элементов списка делим на длину списка
    averageDigits = sumDigits // len(digitalArray)

    # Определяем максимальное значение в списке
    maxValueOfList = max(digitalArray)

    # Новый список
    newList = []

    for _ in range(len(digitalArray)):

        # Добавляем в новый список случайное число, которое больше вычесленного среднего и меньше максимального
        newList.append(random.randrange(averageDigits+1, maxValueOfList))

    print("Результат работы:")
    print("")
    # Целочисленный массив
    print("Целочисленный массив: ", digitalArray)
    print("Среднее арифметическое эдементов массива:", averageDigits)
    print("Максимальное значение среди эдементов массива:", maxValueOfList)
    print("Новый массив: ", newList)

    return


isMinByIndex(digitalArrayForTask5_17_29_41_53, indexForTask5)

exchangeMinMax(digitalArrayForTask5_17_29_41_53)

findMaxInRange(digitalArrayForTask5_17_29_41_53, indexRangeForTask29)

averageModules(digitalArrayForTask5_17_29_41_53)

newList(digitalArrayForTask5_17_29_41_53)
