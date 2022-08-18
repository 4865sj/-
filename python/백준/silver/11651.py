n = int(input())
data = []

for i in range(0, n):
    A = list(map(int, input().split()))
    data.append(A)
    
data.sort(key = lambda x : (x[1], x[0]))

for i in range(0, n):
    print(data[i][0], data[i][1])
