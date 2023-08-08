from random import *
class Saper():
    def play(self):
        while True:
            self.temp_data = input("Введіть коордінати Х та У та коло-во мін через кому\n").split(",")
            if len(self.temp_data) != 3:
                print("має бути три параметри")
                continue
            elif self.temp_data[0].isdigit() != True or self.temp_data[1].isdigit() != True or self.temp_data[2].isdigit() != True:
                print("Данні мають бути цифрами")
                continue
            else:
                break
        self.__data_check(self.temp_data)
        self.__build_mine_field()
        self.__build_game_field()
        print(*self.game_field,sep ="\n")
        self.__main_game()
    def __data_check(self, temp_data):
        self.size_x = int(temp_data[0])
        self.size_y = int(temp_data[1])
        self.mine_count = int(temp_data[2])
        if self.size_x < 1 or self.size_y < 1 or self.mine_count < 1:
            print("Поля та коло-во мін мають бути більше за 1!")
        elif self.mine_count > self.size_y * self.size_x:
            print("Коло-во мін не може бути більше,ніж", self.size_x * self.size_y, "!")
        else:
            return self.size_x, self.size_y, self.mine_count
    def __build_mine_field(self):
        self.field = []
        self.counter_mines = 0
        for i in range(self.size_y):
            self.field.append([])
            for j in range(self.size_x):
                self.field[i].append("0")
        while True:
            self.field[randint(0, self.size_y - 1)][randint(0, self.size_x - 1)] = "*"
            for i in self.field:
                for j in i:
                    if j == "*":
                        self.counter_mines += 1
            if self.counter_mines == self.mine_count:
                break
            else:
                self.counter_mines = 0
        return self.field
    def __build_game_field(self):
        self.game_field = []
        for i in range(self.size_y):
            self.game_field.append([])
            for j in range(self.size_x):
                self.game_field[i].append("-")
        return self.game_field
    def __main_game(self):
        self.total_step_counter = self.size_x * self.size_y - self.mine_count
        self.used_cord = []
        while True:
            while True:
                self.tmp_used_cord = []
                while True:
                    self.answer = input("Введіть коордінати Х та У через запяту \n").split(",")
                    if len(self.answer) != 2:
                        print("Ви маєте передати лише дві координати")
                    elif self.answer[0].isdigit() != True or self.answer[1].isdigit() != True:
                        print("Це мають бути цифри,спробуйте ще")
                        continue
                    else:
                        self.answer_x = int(self.answer[0])
                        self.answer_y = int(self.answer[1])
                        if self.answer_x < 1 or self.answer_x > self.size_x or self.answer_y < 1 or self.answer_y > self.size_y:
                            print("Недоступні координати, спробуйте ще.")
                            continue
                        else:
                            self.tmp_used_cord.append(self.answer_x)
                            self.tmp_used_cord.append(self.answer_y)
                            self.answer_x = self.answer_x - 1
                            self.answer_y = self.answer_y - 1
                            break
                if self.tmp_used_cord in self.used_cord:
                    print("Ви вже використовували ці координати,спробуйте інщі")
                    continue
                else:
                    self.used_cord.append(self.tmp_used_cord)
                    break
            if self.field[self.answer_y][self.answer_x] == "*":
                print("Ви програли :(")
                print(*self.field, sep="\n")
                break
            else:
                self.counter = 0
                self.tmp_field = []
                for x in range(self.answer_x - 1, self.answer_x + 1 + 1):
                    if x < 0:
                        continue
                    elif x > self.size_x - 1:
                        continue
                    for y in range(self.answer_y - 1, self.answer_y + 1 + 1):
                        if y < 0:
                            continue
                        elif y > self.size_y - 1:
                            continue
                        self.tmp_field.append(self.field[y][x])

                for i in self.tmp_field:
                    if i == "*":
                        self.counter += 1
                self.game_field[self.answer_y][self.answer_x] = str(self.counter)
                self.total_step_counter -= 1
                if self.total_step_counter == 0:
                    print("Вітаю, Ви виграли :)")
                    print(*self.field, sep="\n")
                    break
                print(*self.game_field, sep="\n")
Saper().play()