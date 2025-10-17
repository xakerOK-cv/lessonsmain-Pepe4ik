# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import COLOR_YELLOW

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
tochka = 0
# def draw_branches():
#     tochka_X = int(input("Введите точку X: "))
#     tochka_Y = int(input("Введите точку Y: "))
#     ugol = int(input("Введите угол: "))
#     dlinna = int(input("Длинна ветвей: "))
#
#     vector = sd.get_vector((sd.get_point(tochka_X, tochka_Y)), ugol, dlinna, 10)
#     vector.draw()
#     for i in range (5):
#         temp1 = vector.end_point.x
#         temp2 = vector.end_point.y
#         ugol += 30
#         vector = sd.get_vector(sd.get_point(temp1,temp2), ugol, dlinna, 10)
#         vector.draw()
#
#         ugol -= 60
#         vector = sd.get_vector(sd.get_point(temp1,temp2), ugol, dlinna, 10)
#         vector.draw()
        #sd.circle(sd.get_point(temp1,temp2), 2, sd.COLOR_RED, 2)
# КАРОЧЕ БРЕД ЯКИЙСЯ ПОЛУЧИВСЯ ЩАС БУДУ ДЕЛАТЬ НОРМАЛЬНО, Я ИЗУЧИВ ШО ТАКОЕ РЕКУРСИЯ


def draw_branch(tochka, ugol, dlinna):
    if dlinna < 10:
        return
    vector = sd.get_vector(tochka,ugol, dlinna, 2)
    vector.draw()

    tochka_2 = vector.end_point
    draw_branch(tochka_2, ugol + 30, dlinna * 0.75)
    draw_branch(tochka_2, ugol - 30, dlinna * 0.75)


tochka_X = int(input("Введите точку X: "))
tochka_Y = int(input("Введите точку Y: "))
tochka = sd.get_point(tochka_X, tochka_Y)
ugol = int(input("Введите угол: "))
dlinna = int(input("Длинна ветвей: "))


draw_branch(tochka, ugol, dlinna)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


