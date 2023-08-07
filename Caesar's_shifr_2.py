string = [i for i in input().split(" ")]
answer = []
for i in string:
    answer_world = ""
    for j in i:
        temp = [k for k in i if k.isalpha()]
    counter = len(temp)
    for j in i:
        is_upper = "no"
        tmp_word = j.lower()
        if j == j.upper():
            is_upper = "yes"
        if ord(tmp_word) in range(97,122+1):
            if ord(tmp_word) + counter > 122:
                word = chr(ord(tmp_word) + counter - 122-1 + 97)
                if is_upper == "yes":
                    answer_world += word.upper()
                else:
                    answer_world += word
            else:
                word = chr(ord(tmp_word) + counter)
                if is_upper == "yes":
                    answer_world += word.upper()
                else:
                    answer_world += word
        else:
            answer_world += tmp_word
    answer.append(answer_world)
print(*answer)