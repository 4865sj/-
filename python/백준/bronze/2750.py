n = int(input())
data = []

for i in range(0, n):
    a = int(input())
    data.append(a)
    
data.sort()

for i in range(0, n):
    print(data[i])
