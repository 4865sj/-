import math

def prime(n):
    m = 0
    for i in range(2, n):
        if n%i == 0:
            break
        else:
            if i == n-1:
                m += 1
            else:
                pass
    if n == 2:
        m = 1
    else:
        pass
    return m

N = int(input())
data = []
for i in range(0,N):
    a = int(input())
    data.append(a)
    
for i in range(0,N):
    a = data[i]
    b = a//2
    for i in range(0, b):
        c = b-i
        d = b+i
        if prime(c) == 1 and prime(d) == 1:
            print(c, d)
            break
        else:
            continue
