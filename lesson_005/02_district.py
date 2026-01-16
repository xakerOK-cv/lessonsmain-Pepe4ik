# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш ко
from district.soviet_street.house1.room1 import folks as folks1
from district.soviet_street.house1.room2 import folks as folks2
from district.soviet_street.house2.room1 import folks as folks3
from district.soviet_street.house2.room2 import folks as folks4
from district.central_street.house1.room1 import folks as folks5
from district.central_street.house1.room2 import folks as folks6
from district.central_street.house2.room1 import folks as folks7
from district.central_street.house2.room2 import folks as folks8 #импорт всех списков людей из файлов

all_folks = folks1 + folks2 + folks3 + folks4 + folks5 + folks6 + folks7 + folks8 #соединение всех списков воедино

print("На районе живут", ", ".join(all_folks)) #джоин для того чтоб сделать человекочитаемый текст вместро строкового списка

#print("На районе живут", all_folks) #тут просто тест без .join()






