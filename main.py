import random
secret_num = random.randint(1, 100)
print('Попробуйте угадать число от 1 до 100:')
count = 0
while True:
    enter_num = int(input())
    if enter_num > secret_num:
        print('Слишком много, попробуйте еще раз')
        count += 1
    elif enter_num < secret_num:
        print('Слишком мало, попробуйте еще раз')
        count += 1
    elif enter_num == secret_num:
        count += 1
        print(f'Вы угадали, поздравляем! Число было угадано за {count} попыток')
        break