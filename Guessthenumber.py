#Угадай число!

import random

your_guess = 0

number = random.randint(1, 100)
print("Твой компьютер не тянет Skyrim? Не беда, у меня есть развлечение получше. Сегодня мы будем угадывать числа от 1 до 100.")

while your_guess < 10:

    guess = int(input("Как ты думаешь, какое число я загадал? Отвечай осторожно, у тебя всего 10 попыток...\n"))

    your_guess += 1

    if guess < number:
        print("Бери больше!")

    if guess > number:
        print("Бери меньше!")

    if guess == number:
        break

if guess == number:
    print("Невозможно, ты угадал. Признайся честно, ты подглядывал!")
else:
    print("Хаха, тебе не хватило даже 10 попыток, чтобы угадать мое число. Я опять победил! Обожаю эту игру.")