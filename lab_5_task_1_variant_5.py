
import re

# Регулярное выражение требуещее, чтобы в строке было 6 символов и эти символы были числами
ruZipCodeRegex = re.compile('\d{6}')


def checkRuZipCode(zipCode):

    # Если строка в zipCode полностью соответствует регулярному выражению, метод fullmatch вернет НЕ None
    # Значит введенный ZIP code верный и возвращаем True
    if re.fullmatch(ruZipCodeRegex, zipCode) != None:
        return True
    else:
        return False


def validateRuZipCode(zipCode):
    try:
        # Если функция проверки ZIP code, переданного в zipCode, возвращает False
        # Генерируем исключение
        # Иначе, возвращаем ZIP code
        if not checkRuZipCode(zipCode):
            raise ValueError("Аргумент переданный в функцию не верен !")

        return zipCode
    except ValueError as e:
        print(e)


validateRuZipCode("absdef")
validateRuZipCode("123")
validateRuZipCode("123456")
