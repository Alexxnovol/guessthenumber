import random     # подключаем модуль random
print('Добро пожаловать в числовую угадайку')
print('Введите правую границу диапазона(включительно), в котором будет загадано число.')
n = int(input())
secret_num = random.randint(1, n)    # программа загадывает число от 1 до n
def is_valid(enter_num):    # функция проверки корректности введенного пользователем значения
    return enter_num.isdigit() and 1 <= int(enter_num) <= n
def play_game():
    count_attempts = 0    # подсчитываем количество попыток
    while True:  # запускаем бесконечный цикл
        print(f'Введите число от 1 до {n}')
        enter_num = input()
        count_attempts += 1
        if not is_valid(enter_num):  # с помощью функции is_valid проверяем, чтобы число было корректным
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            continue
        else:  # если число корректное, преобразовываем строку к целому числу
            enter_num = int(enter_num)
        if enter_num < secret_num:  # сравниваем введенное число с загаданным
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif enter_num > secret_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif enter_num == secret_num:
            print(f'Вы угадали, поздравляем! Количество попыток: {count_attempts}')
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    print('Сыграть еще раз? y - да, n - нет')
play_game()
replay = input()
while replay == 'y':
    play_game()
