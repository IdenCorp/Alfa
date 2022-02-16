import random
rand = random.randint(1, 10)
print("Угадай целое число от 1 до 10")

def user_chose_lit():
        while True:
            try:

                user_try = int(input("Твой выбор: "))
                if 0 < user_try < 10:
                    return user_try
                print("от 1 до 10")

            except (TypeError, ValueError):
                print("Ты ввёл значение, не являющееся целым числом. Сосредоточься")

user = user_chose_lit()

while user != rand:
    if user > rand:
        print("Твоё число больше загаданного. Попробуй ещё раз.")
    elif user < rand:
        print("Твоё число меньше загаданного. Попробуй ещё раз.")
    user = user_chose_lit()
else:
    print("Ты угадал!")
print("Загаданное число: ", rand)
