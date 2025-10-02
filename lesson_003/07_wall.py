# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from simple_draw import COLOR_RED

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
x_start = 0
y_start = 0
x_start1 = 100
y_start1 = 0
for z in range (3): #кол-во кирпичиков в высоту
    if z %2 == 0: #сдвиг если нечетное значение
        x_start = -50
    else:
        x_start = 0
    x_start1 = x_start + 100
    y_start = y_start1 # чтоб начало следующего кирпичика была на месте конца предыдущего
    y_start1 += 50
    for i in range(10): #кол-во кирпичиков в ширину
        sd.rectangle(sd.get_point(x_start, y_start),sd.get_point(x_start1, y_start1), sd.COLOR_YELLOW, 5 )
        x_start = x_start1
        x_start1 += 100




sd.pause()
