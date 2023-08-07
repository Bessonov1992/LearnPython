file = open("dataset_3363_3.txt")
str = file.read().strip()
str = str.lower()
list_word = str.split()
list_word.sort()
answer = {}
max_counter = 0
max_value = ""
for i in list_word:
    j = [i]
    counter = list_word.count(i)
    answer[i] = counter
for i,j in answer.items():
    if j > max_counter:
        print(i,j)
        max_counter = j
        max_value = i
    else:
        continue
print(max_value,max_counter)