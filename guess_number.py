from random import *
def is_valid_reround(reround):
    if reround in ("y","n","Y","N"):
        return True
    else:
        return False
def is_valid(integer):
    if integer.isdigit() == True and int(integer) in range(1,int(till)+1):
        return True
    else:
        return False
print("Добро пожаловать в числовую угадайку")
reround = "y"
while reround == "y":
    counter = 0
    print("В каком диапазоне будем угадывать число?:)")
    till = input()
    while till.isdigit() == False:
        print("Введите число")
        till = input()
    a = randint(1, int(till)+1)
    while True:
        print("Введите число от 1 до",int(till))
        b = input()
        if is_valid(b) == False:
            print('А может быть все-таки введем целое число от 1 до',int(till),"?")
            continue
        else:
            counter += 1
            b = int(b)
            if b < a:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            elif b > a:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
            else:
                print('Вы угадали, поздравляем!')
                print('Вам понадобилось',counter,'попыток!:)')
                print('Спасибо, что играли в числовую угадайку.')
                break
    print('Хотите еще раз сыграть? Если да - введите "y",нет - введите "n"')
    c = input()
    while True:
        if is_valid_reround(c) == False:
            print('Повторите ввод.Если да - введите "y",нет - введите "n"')
            c = input()
        else:
            if c in ("n","N"):
                reround = "n"
                print("Еще увидимся...:)")
                break
            else:
                reround = "y"
                break