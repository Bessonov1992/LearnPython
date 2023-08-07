file = open("dataset_33630.txt")
a = file.read().strip()
b = []
c = []
max_index = len(a)
counter = 0
next_counter = 1
while counter != max_index:
    if counter >= max_index or next_counter>= max_index:
        b.append(int(a[counter]))
        break
    elif a[counter] in ("0","1","2","3","4","5","6","7","8","9") and a[next_counter] in ("0","1","2","3","4","5","6","7","8","9"):
        d = a[counter]+a[next_counter]
        b.append(int(d))
        counter += 2
        next_counter +=2
    elif a[counter] in ("0","1","2","3","4","5","6","7","8","9"):
        b.append(int(a[counter]))
        counter+=1
        next_counter+=1
    else:
        c.append(a[counter])
        counter+=1
        next_counter += 1
counter_b = 0
max_index_b = len(b)
answer = ""
while counter_b != max_index_b:
    answer+=(c[counter_b]*b[counter_b])
    counter_b+=1
print(answer)
ans_file = open("dataset_33630_ans.txt", "w")
ans_file.write(answer.strip())