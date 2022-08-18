n = int(input())

data = list(map(int, input().split()))
temp = list(set(data))
temp.sort()

dic = {temp[i]:i for i in range(0, len(temp))}

for x in data:
    print(dic[x], end=" ")
