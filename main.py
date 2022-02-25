import random, time

class Rules:
    #родительский класс; тут я также собрал сообщение "главного меню" и проверки
    beg = 1
    end = 10
    rand = random.randint(beg, end)

    def main_menu(self):
        #фиксированное сообщение "главного меню"; мне кажется, на текущий момент, так её зафиксировать удобнее
        print("Список игр:\n1 - Я загадываю число, ты пытаешься угадать\n2 - Ты загадываешь число, я пытаюсь угадать\nexit - Выход")

    def user_chose_lit(self):
        #ввод и проверка значения пользователя для game_1
        while True:
            try:
                user_try = int(input("Твоё число: "))
                if 1 <= user_try <= 10:
                    return user_try
                else:
                    print("Загаданное число от 1 до 10. Не увлекайся.")
            except (TypeError, ValueError):
                print("Ты ввёл значение, не являющееся целым числом. Сосредоточься.")

class Games(Rules):
    def game_1(self):
        #игра из первого задания - мы угадываем число программы
        print("Угадай целое число от 1 до 10")
        user = Rules.user_chose_lit(self)
        while user != Rules.rand:
            #пользователь вводит значения пока не угадает загаданное число
            if user > Rules.rand:
                print("Твоё число больше загаданного. Попробуй ещё раз.")
            elif user < Rules.rand:
                print("Твоё число меньше загаданного. Попробуй ещё раз.")
            user = Rules.user_chose_lit(self)
        else:
            print("Ты угадал!")
        print("Загаданное число: ", Rules.rand, "\n")
        time.sleep(1) #здесь и далее я сделал задержки для красоты, чтобы разделить вывод информации

    def game_2(self):
        #игра из второго задания - программа угадывает наше число
        print("Загадай целое число от 1 до 10. Даю тебе пару секунд на это.")
        time.sleep(2)
        print("Ты загадал число ", Rules.rand)
        user = input("Я угадал? ")
        #падает, если играть нечестно по отношению к программе; я не догадался, как сделать проверку, чтобы это не заваливалось в зацикливание или вылеты с ValueError
        #возможно, стоило подойти к этому вообще по другому, например, складывать граничные значения и делить на 2, а не сужать диапозон рандома
        while user != '=':
                    if user == '>':
                        Rules.beg = Rules.rand + 1
                    elif user == '<':
                        Rules.end = Rules.rand - 1
                    Rules.rand = random.randint(Rules.beg, Rules.end)
                    print("Значит это ", Rules.rand)
                    user = input("Я угадал? ")
        else:
            print("Какой я молодец!\n")
            time.sleep(1)

#"интерфейс" программы - здесь нам выводятся опции "главного меню"
print("Давай сыграем в одну из игр.")
Rules.main_menu(Rules) #я эту конструкцию праивльно строю? выглядит как будто не очень
user = input("Что выберешь? ")
while user != 'exit':
    if user == '1':
        Games.game_1(Rules)
    elif user == '2':
        Games.game_2(Rules)
    else:
        print("Эта игра появится с ближайшим обновлением.\n")
    print("Попробуем ещё?")
    Rules.main_menu(Rules)
    user = input("Твой выбор: ")

else:
    SystemExit









