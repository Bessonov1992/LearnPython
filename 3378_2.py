import requests

answer = 0
file = open('dataset_3378_2.txt')
a = file.read().strip()
b = requests.get(a)
c = b.text.splitlines()
for i in c:
    answer += 1
print(answer)
print(a)
