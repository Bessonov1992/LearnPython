
def if_valid_option(option):
    if option.lower() in ("шифровать","дешифровать"):
        return True
    else:
        return False
def if_valid_lang(lang):
    if lang.lower() in ("англ","рус"):
        return True
    else:
        return False
def if_valid_side(step):
    if step.isdigit():
        return True
    else:
        return False
option = input("Если хотите зашифровать - введите 'шифровать',если дешифровать - 'дешифровать'\n")
while True:
    if if_valid_option(option) == False:
        option = input("Если хотите зашифровать - введите 'шифровать',если дешифровать - 'дешифровать'\n")
    else:
        break
language = input("Введите язык 'англ' или'рус'.\n")
while True:
    if if_valid_lang(language) == False:
        language = input("Введите язык 'англ' или'рус'.\n")
    else:
        break
step = input("Какой шаг шифрования?Введите цифру которая не больше коло-ва букв в алфавите\n")
while True:
    if if_valid_side(step) == False:
        step = input("Какой шаг шифрования?Введите цифру которая не больше коло-ва букв в алфавите\n")
    elif language == "англ" and (int(step) < 0 or int(step) > 26):
        step = input("Какой шаг шифрования?Введите цифру которая не больше коло-ва букв в алфавите\n")
    elif language == "рус" and (int(step) < 0 or int(step) > 32):
        step = input("Какой шаг шифрования?Введите цифру которая не больше коло-ва букв в алфавите\n")
    else:
        break
start,stop,object,answer = 0,0,input("Введите текст\n"),''
if language == "англ":
    start,stop = 96,122
else:
    start,stop = 1071,1103
if option == "шифровать":
    for i in object:
        is_upper = "no"
        tmp_word = i.lower()
        if i == i.upper():
            is_upper = "yes"
        if ord(tmp_word) in range(start + 1, stop + 1):
            if ord(tmp_word)+int(step) > stop:
                word = chr(ord(tmp_word) + int(step) - stop + start)
                if is_upper == "yes":
                    answer += word.upper()
                else:
                    answer += word
            else:
                word = chr(ord(tmp_word)+ int(step))
                if is_upper == "yes":
                    answer += word.upper()
                else:
                    answer += word
        else:
            answer += i
elif option == "дешифровать":
    for i in object:
        is_upper = "no"
        tmp_word = i.lower()
        if i == i.upper():
            is_upper = "yes"
        if ord(tmp_word) in range(start+1,stop+1):
            if ord(tmp_word)-int(step) < start+1:
                word = chr(ord(tmp_word) - int(step) + stop - start)
                if is_upper == "yes":
                    answer += word.upper()
                else:
                    answer += word
            else:
                word = chr(ord(tmp_word) - int(step))
                if is_upper == "yes":
                    answer += word.upper()
                else:
                    answer += word
        else:
            answer += i
print(answer)
