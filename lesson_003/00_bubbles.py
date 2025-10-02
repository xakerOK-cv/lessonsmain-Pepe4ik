# -*- coding: utf-8 -*-
import random
import simple_draw as sd
from simple_draw import COLOR_CYAN

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

#sd.circle(sd.get_point (600,300), 100, [190,190,199],3)
#sd.circle(sd.get_point (600,300), 105, [190,190,199],3)# ну вот, шаг в 5 пикселей раз
#sd.circle(sd.get_point (600,300), 110, [190,190,199],3)# и два, готово?

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
# def draw_bubbles(point, shag):
#     radius_shag = 100 + shag
#     sd.circle(point, 100, COLOR_CYAN, 3)
#     sd.circle(point, radius_shag, COLOR_CYAN, 3)
# x = int(input("Введите первую координату точки рисования: "))
# y = int(input("Введите вторую координату точки рисования: "))
# shag = int(input("Введите шаг между радиусами окружностей: "))
# point = sd.get_point(x, y)
# draw_bubbles(point,shag)

#не второпаю, шаг тут это радиус или все-таки чето связанное с точкой центра окружности
#но вроде сделал, класс


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# x = 100
# for i in randint (10):
#     sd.circle(sd.get_point(x,200), 30, COLOR_CYAN, 3)
#     x += 60
#ну вроде правильно, все как сказано в ТЗ

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# x= 100
# y = 100
# for n in randint (4):
#     y += 60
#     x = 100
#     for i in randint (10):
#         sd.circle(sd.get_point(x,y), 30, COLOR_CYAN, 3)
#         x += 60

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for i in range(100):
    sd.circle(sd.get_point(random.randint(70,1200),random.randint(70,500)),30, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
sd.pause()

# работает ! ОК

