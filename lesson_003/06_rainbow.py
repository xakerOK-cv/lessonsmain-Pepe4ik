# -*- coding: utf-8 -*-
from sys import exec_prefix

# (цикл for)

import simple_draw as sd
from simple_draw import COLOR_RED

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# x_start = 50
# y_start = 50
# x_end = 350
# y_end = 450
# for color in rainbow_colors:
#     sd.line(sd.get_point(x_start,y_start),sd.get_point(x_end,y_end),color,4)
#     y_start -= 5
#     y_end -= 5

    #x_start += 5 #необязательно?
    #x_end += 5 #необязательно?
#ВОПРОС: ну вот что значит "с шагом 5" ? делать шаг по всем координатам или только по Y?
#лучше выглядит без изменения значений X

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
x_circle = 300
y_circle = 0
radius = 250
for color in rainbow_colors:
    sd.circle(sd.get_point(x_circle,y_circle),radius,color,10)
    #y_circle += 2
    radius += 9

sd.pause()
