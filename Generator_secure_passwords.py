from random import *
def is_valid_answer(answer):
    if answer.lower() in ("да","нет"):
        return True
    else:
        return False
def is_digit(answer):
    if answer.isdigit() == False:
        return False
    elif int(answer) <= 0:
        return False
    else:
        return True
def generate_password(leight,chars):
    password = ""
    for i in range(int(leight)):
        password += chars[randint(0,len(chars)-1)]
    print(password)
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
how_many = input("Сколько паролей нужно сгенерировать?\n")
while is_digit(how_many) != True:
    how_many = input("Сколько паролей нужно сгенерировать? Введите цифру от 1\n")
len_pass = input("Насколько длинным должен быть каждый пароль?\n")
while is_digit(len_pass) != True:
    len_pass = input("Насколько длинным должен быть каждый пароль?Введите цифру от 1\n")
is_digit = input("Включить цифры в пароль?\n")
while is_valid_answer(is_digit) != True:
    is_digit = input("Включить цифры в пароль?Введите да или нет\n")
if is_digit.lower() == "да":
    chars += digits
is_upper_words = input("Включить ли заглавные буквы англ. алфавита в пароль?\n")
while is_valid_answer(is_upper_words) != True:
    is_upper_words = input("Включить ли заглавные буквы англ. алфавита в пароль?Введите да или нет\n")
if is_upper_words == "да":
    chars += uppercase_letters
is_lower_words = input("Включить ли строковые буквы англ. алфавита в пароль?\n")
while is_valid_answer(is_lower_words) != True:
    is_lower_words = input("Включить ли строковые буквы англ. алфавита в пароль?Введите да или нет\n")
if is_lower_words == "да":
    chars += lowercase_letters
is_spec_symbols = input("Включить ли символы '!#$%&*+-=?@^_' в пароль?\n")
while is_valid_answer(is_spec_symbols) != True:
    is_spec_symbols = input("Включить ли символы '!#$%&*+-=?@^_' в пароль?Введите да или нет\n")
if is_spec_symbols == "да":
    chars += punctuation
is_not_ord_symbols = input("Исключать ли неоднозначные символы 'il1Lo0O'?\n")
while is_valid_answer(is_not_ord_symbols) != True:
    is_not_ord_symbols = input("Исключать ли неоднозначные символы 'il1Lo0O'?Введите да или нет\n")
if is_not_ord_symbols == "да":
    chars_list = [i for i in chars if i not in ("i","l","1","L","o","0","O","0")]
    chars = ""
    for i in chars_list:
        chars += i
for i in range(int(how_many)):
    if is_upper_words.lower() == "нет" and is_digit.lower() == "нет" and is_lower_words.lower() == "нет" and is_spec_symbols.lower() == "нет":
        print("Невозможно составить пароль из ничего. Начните сначала")
        break
    else:
        generate_password(len_pass,chars)