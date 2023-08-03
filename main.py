import random    # подключаем модуль random
print('Добро пожаловать в числовую угадайку')
print('В игре есть два режима. Стандартный режим: я загадываю число от 1 до 100 включительно.\n'
          'Пользовательский режим: вы сами задаете диапазон, в котором хотите угадывать число.')
def game_mode_selection():    # функция выбора режима игры
    print('Введите 1 или 2 в зависимости от своего выбора режима игры. 1 - стандартный режим. 2 - пользовательский.')
    game_mode = input()
    while game_mode != '1' and game_mode != '2':
        print('Необходимо ввести 1 или 2.')
        game_mode = input()
    if game_mode == '1':
        play_standard_game_mode()
    elif game_mode == '2':
        play_custom_game_mod()

def replay_or_quit():    # функция повторной игры или выхода из программы
    print('Спасибо, что играли в числовую угадайку! Если хотите сыграть еще раз, введите 3.')
    replay = input()
    if replay == '3':
        game_mode_selection()
    else:
        print('Работа программы завершена!')
def is_valid(enter_name, left, right):    # функция проверки на валидность
    return enter_name.isdigit() and int(left) <= int(enter_name) <= int(right)
def play_standard_game_mode():    # функция стандартного режима
    secret_name = random.randint(1, 100)
    count_attempts = 0
    while True:
        print('Введите число в диапазоне от 1 до 100 включительно.')
        enter_name = input()
        if not is_valid(enter_name, 1, 100):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            enter_name = int(enter_name)
        if enter_name < secret_name:
            count_attempts += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif enter_name > secret_name:
            count_attempts += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif enter_name == secret_name:
            count_attempts += 1
            print(f'Вы угадали, поздравляем! Количество попыток: {count_attempts}')
            replay_or_quit()
            break
def play_custom_game_mod():    # функция пользовательского режима
    print('Введите левую границу диапазона(от)')
    left_border = input()
    while not left_border.isdigit():
        print('Необходимо ввести число.')
        left_border = input()
    print('Введите правую границу диапазона(до)')
    right_border = input()
    while not right_border.isdigit():
        print('Необходимо ввести число')
        right_border = input()
    secret_name = random.randint(int(left_border), int(right_border))
    count_attempts = 0
    while True:
        print(f'Введите число в диапазоне от {left_border} до {right_border} включительно')
        enter_name = input()
        if not is_valid(enter_name, left_border, right_border):
            print(f'А может все таки введем целое число от {left_border} до {right_border}?')
            continue
        else:
            enter_name = int(enter_name)
        if enter_name < secret_name:
            count_attempts += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif enter_name > secret_name:
            count_attempts += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif enter_name == secret_name:
            count_attempts += 1
            print(f'Вы угадали, поздравляем! Количество попыток: {count_attempts}.')
            replay_or_quit()
            break
game_mode_selection()
