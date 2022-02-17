import random
rand = random.randint(1, 10)
print("Угадай целое число от 1 до 10")

def user_chose_lit():
        """ввод и проверка значения пользователя"""
        while True:
            try:
                user_try = int(input("Твой выбор: "))
                if 1 <= user_try <= 10:
                    return user_try
                else:
                    print("Загаданное число от 1 до 10. Не увлекайся.")
            except (TypeError, ValueError):
                print("Ты ввёл значение, не являющееся целым числом. Сосредоточься.")

user = user_chose_lit()

while user != rand:
    """пользователь вводит значения пока не угадает загаданное число"""
    if user > rand:
        print("Твоё число больше загаданного. Попробуй ещё раз.")
    elif user < rand:
        print("Твоё число меньше загаданного. Попробуй ещё раз.")
    user = user_chose_lit()
else:
    print("Ты угадал!")
print("Загаданное число: ", rand)
