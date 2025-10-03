# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


# TODO здесь ваш код



# for i in range(10):
#     sd.line(sd.get_point(a_start,b_start), sd.get_point(a_end,b_end), sd.COLOR_YELLOW, 4)
#     a_start = a_end
#     b_start = b_end
#     a_end = a_end + 20
#     b_end = b_end + 3
#тут короче тригонометрию надо использовать, хочу побольше заданий сделать поэтому воздержусь

x1, y1 = 100, 120
x2, y2 = 125, 115
x3, y3 = 175, 115
x4, y4 = 200, 120


x5, y5 = 115, 190
x6, y6 = 150 , 150
x7, y7 = 185, 190
x8, y8 = 150 , 150

circle_x, circle_y = 150, 150
for i in range(10):
    random_variable = rd.randint(-100, 500)
    random_variable2 = rd.randint(-100, 500)

    x1, y1 = x1 + random_variable, y1 + random_variable2
    x2, y2 = x2+random_variable, y2+random_variable2
    x3, y3 = x3+random_variable, y3+random_variable2
    x4, y4 = x4+random_variable, y4+random_variable2

    x5, y5 = x5+random_variable, y5+random_variable2
    x6, y6 = x6+random_variable, y6+random_variable2
    x7, y7 = x7+random_variable, y7+random_variable2
    x8, y8 = x8+random_variable, y8+random_variable2
    circle_x, circle_y = circle_x + random_variable, circle_y + random_variable2

    sd.line(sd.get_point(x1, y1), sd.get_point(x2, y2), sd.COLOR_YELLOW, 4)
    sd.line(sd.get_point(x2, y2), sd.get_point(x3, y3), sd.COLOR_YELLOW, 4)
    sd.line(sd.get_point(x3, y3), sd.get_point(x4, y4), sd.COLOR_YELLOW, 4)
    sd.line(sd.get_point(x5, y5), sd.get_point(x5, y6), sd.COLOR_YELLOW, 4)
    sd.line(sd.get_point(x7, y7), sd.get_point(x7, y8), sd.COLOR_YELLOW, 4)

    x1, y1 = 100, 120
    x2, y2 = 125, 115
    x3, y3 = 175, 115
    x4, y4 = 200, 120

    x5, y5 = 115, 190
    x6, y6 = 150, 150
    x7, y7 = 185, 190
    x8, y8 = 150, 150

    sd.circle(sd.get_point(circle_x, circle_y), 80, sd.COLOR_YELLOW, 4)
    circle_x, circle_y = 150, 150


sd.pause()
