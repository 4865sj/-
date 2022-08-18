import math

def prime(n):
    k = int(math.sqrt(2*n))
    A = [True]*(2*n + 1)
    for i in range(2, k+1):
        if A[i] == True:
            for j in range(2*i, 2*n + 1, i):
                A[j] = False
    m=0
    for i in range(n+1, 2*n + 1):
        if A[i] == True:
            m += 1
            
    return m

data = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        data.append(a)
        
n = len(data)

for i in range(0, n):
    print(prime(data[i]))
        
    
