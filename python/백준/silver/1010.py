def comb(n, r):
    p = 1
    q = 1
    i = 0
    j = 1
    while i < r:
        p = p*(n-i)
        i += 1
        
    while j <= r:
        q = q*j
        j += 1
    
    return p//q

n = int(input())
data = []
for i in range(0, n):
    A = list(map(int, input().split()))
    data.append(A)
    
for i in range(0, n):
    A = data[i]
    print(comb(A[1], A[0]))
    
