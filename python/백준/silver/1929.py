import math
m, n = map(int, input().split())

k = int(math.sqrt(n))
data = [True]*(n+1)

for i in range(2, k+1):
    if data[i] == True:
        for j in range(2*i, n+1, i):
            data[j] = False
            
data[1] = False
            
for i in range(m, n+1):
    if data[i] == True:
        print(i)
