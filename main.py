def prog1():
    words = []
    while (new_word := str(input())) != "stop":
        words.append(new_word)
    print(" ".join(words))


def prog2():
    words = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Редкое слово")
        else:
            print("Не очень редкое слово")


def prog3():
    import random
    k = 0
    while k<3:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        print(a, "+", b, "=")
        res = int(input())
        if res == a + b:
            print('Правильно')
        else:
            print('Неправильно')
            k += 1
    else:
        print('Игра окончена')

prog1()
prog2()
prog3()