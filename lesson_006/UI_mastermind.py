import engine_mastermind as engine

engine.загадать_число()
number_of_user_inputs = 0
while True:
    print(engine.numbers) #просто подсказка которую можно забрать
    user_input = str(input("Введите число: "))
    result = engine.проверить_число(user_input)
    print(result)
    number_of_user_inputs += 1
    if result["bulls"] == 4:
        print("Вы угадали, кол-во ходов: ", number_of_user_inputs)
        while True:
            answer = str(input("Хотите еще партию?: y/n"))
            if answer == "y":
                number_of_user_inputs = 0
                engine.загадать_число()
                break
            elif answer == "n":
                exit()
            else:
                print("Введите y/n")