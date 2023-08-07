a = open("dataset_3363_4.txt")
counter = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0
ans = ""
for i in a:
    counter += 1
    tmp = []
    for j in i.split(";"):
        if j[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            tmp.append(int(j))
        else:
            tmp.append(j)
    tmp_ans = str(round((int(tmp[-1]) + int(tmp[-2]) + int(tmp[-3])) / 3, 9)) + "\n"
    ans += tmp_ans
    sum_1 += int(tmp[-3])
    sum_2 += int(tmp[-2])
    sum_3 += int(tmp[-1])
ans = ans + str(round(sum_1 / counter, 9)) + " " + str(round(sum_2 / counter, 9)) + " " + str(round(sum_3 / counter, 9))
ans_file = open("dataset_3363_4_ans.txt", "w")
print(ans)
ans_file.write(ans.strip())
