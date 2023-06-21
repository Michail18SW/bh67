from random import randint


def quess_the_number():
    attempts = 0
    number = randint(1, 100)
    while True:
        quess = int(input('Введите число от 1 до 100: '))
        attempts += 1
        if quess < number:
            print('Загаданное число больше')
        elif quess > number:
            print('Загаданное число меньше')
        else:
            print(f'Поздравляю! Вы угадали загаданное число :) У вас на это ушло {attempts} попыток.')
            break


quess_the_number()
