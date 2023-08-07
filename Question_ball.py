from random import *
def is_valid_reround(reround):
    if reround.lower() in ("да","нет"):
        return True
    else:
        return False
def is_valid_question(question):
    if question[-1] == "?":
        return True
    else:
        return False
again = "yes"
answer_list = ["Бесспорно","Предрешено","Никаких сомнений","Определённо да","Можешь быть уверен в этом",
               "Мне кажется - да","Вероятнее всего","Хорошие перспективы","Знаки говорят - да","Да",
               "Пока неясно, попробуй снова","Спроси позже","Лучше не рассказывать","Сейчас нельзя предсказать","Сконцентрируйся и спроси опять",
               "Даже не думай","Мой ответ - нет","По моим данным - нет","Перспективы не очень хорошие","Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input("Как Вас зовут?\n")
print("Привет",name,"!;)")
while again == "yes":
    answer = input("Задайте мне корректный вопрос :)\n")
    if is_valid_question(answer) == True:
        print(choice(answer_list))
        more = input("Хотели бы еще задать мне вопрос?Если да - введите 'да',нет - введите 'нет':)\n")
        while True:
            if is_valid_reround(more) == True:
                if more.lower() == "да":
                    break
                else:
                    print("Возвращайся если возникнут вопросы!")
                    again = "no"
                    break
            else:
                print("Введите 'да' или 'нет'")
                more = input()
                continue
    else:
        continue