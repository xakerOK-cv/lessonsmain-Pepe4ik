# -*- coding: utf-8 -*-

import simple_draw as sd
import math

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# ТРЕУГОЛЬНИК
def triangle():

    vector_start1, vector_start2 = 300,300 # начало откуда будет рисоваться вся фигура
    vector_angle = 90 #нужно для того чтоб изменить куда будет смотреть первый вектор ну и соответственно вся фигура
    for i in range (3): # кол-во сторон
        vector = sd.get_vector(sd.get_point(vector_start1,vector_start2),vector_angle,90, 3)
        #print(vector.end_point)

        vector_angle += 120
        vector.draw(sd.COLOR_YELLOW,2)
        vector_start1, vector_start2 = vector.end_point.x, vector.end_point.y

#КВАДРАТ
def rectangle ():
    vector_start1, vector_start2 = 400,400 # начало откуда будет рисоваться вся фигура
    vector_angle = 90 #нужно для того чтоб изменить куда будет смотреть первый вектор ну и соответственно вся фигура
    for i in range (4): # кол-во сторон
        vector = sd.get_vector(sd.get_point(vector_start1,vector_start2),vector_angle,90, 3)
        #print(vector.end_point)

        vector_angle += 90
        vector.draw(sd.COLOR_YELLOW,2)
        vector_start1, vector_start2 = vector.end_point.x, vector.end_point.y
def pentagon():
    vector_start1, vector_start2 = 200, 200  # начало откуда будет рисоваться вся фигура
    vector_angle = 90  # нужно для того чтоб изменить куда будет смотреть первый вектор ну и соответственно вся фигура
    for i in range(5):  # кол-во сторон
        vector = sd.get_vector(sd.get_point(vector_start1, vector_start2), vector_angle, 90, 3)
        # print(vector.end_point)

        vector_angle += 72
        vector.draw(sd.COLOR_YELLOW, 2)
        vector_start1, vector_start2 = vector.end_point.x, vector.end_point.y
def hexagon():
    side_Q = 6                # количество сторон
    radius = 90               # радиус окружности
    cx, cy = 200, 300         # центр фигуры
    angle_start = 90          # стартовый угол (в градусах)

    # вычисляем все вершины по окружности
    vertices = []
    for i in range(side_Q):
        angle_rad = math.radians(angle_start + i * 360 / side_Q)
        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)
        vertices.append((x, y))

    # рисуем стороны через get_vector
    for i in range(side_Q):
        start_x, start_y = vertices[i]
        end_x, end_y = vertices[(i + 1) % side_Q]  # следующая вершина, % для замыкания
        # длина и угол для get_vector
        dx = end_x - start_x
        dy = end_y - start_y
        length = math.hypot(dx, dy)
        angle = math.degrees(math.atan2(dy, dx))
        vector = sd.get_vector(sd.get_point(int(start_x), int(start_y)), angle, length, 3)
        vector.draw(sd.COLOR_YELLOW, 2)
triangle()
rectangle()
pentagon()
hexagon()
# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
