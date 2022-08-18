import sys

n = int(sys.stdin.readline())
data = []

for i in range(0, n):
    A = list(map(int, sys.stdin.readline().split()))
    data.append(A)

data.sort(key = lambda x: (x[0],x[1]))

for i in range(0, n):
    print(data[i][0], data[i][1])
