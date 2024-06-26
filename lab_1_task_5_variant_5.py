#
# Задание 5. Дана строка. Необходимо найти все даты, которые описаны в виде "31 февраля 2007".
#

inputString = "Сегодня 03.01.2034, 28-09-1948 или 27 марта 2024..."

# Создаем массив возможных дней месяца, "1", "2", "3" ... "31"
dateRange = [str(date) for date in range(1, 32)]

# Создаем массив возможных годов, "1100", "1101", "1102" ... "2100"
mounthRange = ["декабря", "января", "февраля", "марта", "апреля",
               "мая", "июня", "июля", "августа", "сентября", "октября"]

# Создаем массив возможных годов, "1000", "1001", "1002" ... "3000"
yearRange = [str(year) for year in range(1000, 3001)]

# Очищаем текстовую строку от точек и запятых.
clearedInputString = inputString.replace(".", "").replace(",", "")

# Разбиваем строку по словам и помещаем в список
listByWord = clearedInputString.split(" ")


# проходим по списку со 2-го элемента до конца
for index in range(2, len(listByWord)):

    # Предполагаем, что слово по индекс-2 - это день
    day = listByWord[index - 2]
    # Предполагаем, что слово по индекс-1 - это месяц
    nounth = listByWord[index - 1]
    # Предполагаем, что слово по индексу - это год
    year = listByWord[index]

    # Если слово в day входит в список дней
    if day in dateRange:
        # Если слово в nounth входит в список месяцев
        if nounth in mounthRange:
            # Если слово в year входит в список годов
            if year in yearRange:

                # Значит найдена комбинация трех слов, описывающая дату в виде "31 февраля 2007"
                print(day, nounth, year)
