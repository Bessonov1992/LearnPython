a = int(input())
b = [i for i in range(1,a**2+1)]
field = [[] for i in range(a)]
print(b)
print(*field,sep="\n")