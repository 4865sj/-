n = int(input())
data = []

for i in range(0, n):
    a = input()
    if a in data:
        pass
    else:
        data.append(a)
        
data.sort()
data.sort(key=len)

for x in data:
    print(x)
