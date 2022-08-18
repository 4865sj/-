n = int(input())
data = []

for i in range(0, n):
    A = list(input().split())
    A[0] = int(A[0])
    data.append(A)
    
data.sort(key = lambda x : x[0])

for x in data:
    print(x[0], x[1])
