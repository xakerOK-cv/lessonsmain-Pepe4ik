
brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

if brick_x <= hole_x:
    print('good x1')
    if brick_y <= hole_y:
        print("good x2")
        if brick_z <= hole_x and hole_y:
            print('good x3')
    else:
        if brick_z <= hole_x and hole_y:
            print('good x33')
else:
    if brick_y <= hole_y:
        print("good x22")
        if brick_z <= hole_x and hole_y:
            print('good x333')
    else:
        if brick_z <= hole_x and hole_y:
            print('good x3333')

# OK



