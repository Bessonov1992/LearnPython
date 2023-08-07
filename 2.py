list = input().split()
len_list = len(list)
tmp_len_list = len_list
answer = []
answer_2 = []
while len_list != 0:
    for i in range(len_list+1):
        if list[:i] in answer[i-1:i+1]:
            continue
        else:
            answer.append(list[:i])
    del list[0]
    len_list = len(list)
answer = answer
print(answer)
while tmp_len_list != 0:
    for i in range(tmp_len_list+1):
        for j in answer:
            if len(j) == i:
                if j in answer_2:
                    continue
                else:
                    answer_2.append(j)
    tmp_len_list -= 1
print(answer_2)