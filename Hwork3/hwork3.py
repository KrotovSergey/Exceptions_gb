# Фамилия Имя Отчество датарождения номертелефона пол
# Форматы данных:
# фамилия, имя, отчество - строки
# дата_рождения - строка формата yyyy-yy-mm
# номер_телефона - целое беззнаковое число без форматирования //
# пол - символ латиницей f или m.

import datetime

# class LenDataError(Exception):
#     pass
#
# class DateError(Exception):
#     pass
#
# class TypeErr(Exception):
#     pass


class DataError(Exception):
    pass


data_str = input(
    "Введите Фамилию, Имя , Отчество, дату рождения формата yyyy-mm-dd, номер телефона, пол через пробел \n")
data = data_str.split(" ")

if len(data) != 6:
    raise DataError('введено не верное количество полей')

try:
    datetime.date.fromisoformat(data[3])
except ValueError:
    raise DataError("неверный формат даты , должен быть  YYYY-MM-DD")

if not data[4].isdigit():
    raise DataError("неверный формат телефона")

if data[5] == "f" or data[5] == "m":
    pass
else:
    raise DataError("неверный пол")

try:
    with open(data[0], 'a') as fileToSave:
        fileToSave.write(data_str+"\n")
except:
    raise DataError("невозмжно записать файл")
