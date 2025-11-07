 # -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
snowflakes_list = []
sugrob_list = []
for i in range(N):
    x = random.randint(20, 600) # Координата X
    y = random.randint( 20,700) # Координата Y
    z = random.randint(10,100)# Длинна снежинки
    snowflakes_list.append([x,y,z])

while True:
    for snowflake_sugrob in sugrob_list:
        sd.snowflake(sd.get_point(snowflake_sugrob[0], snowflake_sugrob[1]), snowflake_sugrob[2], sd.COLOR_WHITE)

    for snowflake in snowflakes_list: # Стирание старых
        sd.snowflake(sd.get_point(snowflake[0], snowflake[1]), snowflake[2], sd.background_color)
    for snowflake in snowflakes_list: # Смещение
        snowflake[1] -= 5
        snowflake[0] = snowflake[0] + random.randint(-6,6)
    for snowflake in snowflakes_list: # рисование

        sd.snowflake(sd.get_point(snowflake[0], snowflake[1]),snowflake[2], sd.COLOR_WHITE )



    sd.sleep(0.03)
    for snowflake in snowflakes_list:
        if snowflake[1] <= -10:
            sugrob_list.append(list(snowflake)) #создание нового списка снежинки в котором будут потом отдельно отрисовываться


            snowflake[1] = random.randint(600, 700)#телепортация снежинки рандомно вверх
            snowflake[0] = random.randint(20, 600)

    for snowflake_sugrob in sugrob_list:#для отрисовки когда следующие снежинки зарисовываются цветом заднего фона и тем самым зарисовывают то что в сугробе
        sd.snowflake(sd.get_point(snowflake_sugrob[0], snowflake_sugrob[1]), snowflake_sugrob[2], sd.COLOR_WHITE)

    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку



