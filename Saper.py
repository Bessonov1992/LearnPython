from random import *
def is_valid_number(number):
    if number.isdigit() != True :
        return False
    else:
        return True
field = []
counter_mines = 0
used_cord = []
while True:
    size_y = input("Введіть коло-во строк поля від 1 \n")
    if is_valid_number(size_y) == False or int(size_y) == 0:
        continue
    else:
        size_y = int(size_y)
        break
while True:
    size_x = input("Введіть коло-во стобчиків поля від 1\n")
    if is_valid_number(size_x) == False or int(size_x) == 0:
        continue
    else:
        size_x = int(size_x)
        break
while True:
    count_mines = input("Введіть кілкість мін на полі\n")
    if is_valid_number(count_mines) == False:
        print("Вибачте,ви маєте задати цифру від 1 до",size_y * size_x)
        continue
    elif int(count_mines) == 0:
        print("Вибачте,мін не може бути меньше 1")
        continue
    elif int(count_mines) >= size_y * size_x:
        print("Вибачте,мін більше ніж може бути на полі")
        continue
    else:
        count_mines = int(count_mines)
        break
for i in range(size_y):
    field.append([])
    for j in range(size_x):
        field[i].append("0")
while True:
    field[randint(0,size_y-1)][randint(0,size_x-1)] = "*"
    for i in field:
        for j in i:
            if j == "*":
                counter_mines += 1
    if counter_mines == count_mines:
        break
    else:
        counter_mines = 0
game_field = []
for i in range(size_y):
    game_field.append([])
    for j in range(size_x):
        game_field[i].append("-")
print(*game_field,sep = "\n")
#print(*field,sep = "\n")           # Підказка для отладки
total_step_counter = size_x * size_y - count_mines
while True:
    while True:
        tmp_used_cord = []
        while True:
            answer_x = input("Введіть коордінату 'X'\n")
            if is_valid_number(answer_x) == False or int(answer_x) == 0 or int(answer_x) > size_x:
                print("Недопустима координата,повторіть ввод ще раз")
                continue
            else:
                tmp_used_cord.append(answer_x)
                answer_x = int(answer_x)-1
                break
        while True:
            answer_y = input("Введіть коордінату 'Y'\n")
            if is_valid_number(answer_y) == False or int(answer_y) == 0 or int(answer_y) > size_y:
                print("Недопустима координата,повторіть ввод ще раз")
                continue
            elif answer_y == 0:
                continue
            else:
                tmp_used_cord.append(answer_y)
                answer_y = int(answer_y) - 1
                break
        if tmp_used_cord in used_cord:
            print("Ви вже використовували ці координати,спробуйте інщі")
            continue
        else:
            used_cord.append(tmp_used_cord)
            break

    if field[answer_y][answer_x] == "*":
        print("Ви програли :(")
        print(*field, sep="\n")
        break
    else:
        counter = 0
        tmp_field = []
        for x in range(answer_x-1,answer_x+1+1):
            if x < 0:
                continue
            elif x > size_x-1:
                continue
            for y in range(answer_y-1,answer_y+1+1):
                if y < 0:
                    continue
                elif y > size_y-1:
                    continue
                tmp_field.append(field[y][x])

        for i in tmp_field:
            if i == "*":
                counter += 1
        game_field[answer_y][answer_x] = str(counter)
        total_step_counter -= 1
        if total_step_counter == 0:
            print("Вітаю, Ви виграли :)")
            print(*field, sep="\n")
            break
        print(*game_field,sep = "\n")