def gcd(a, b):
    if b%a == 0:
        return a
    else:
        c = b%a
        return gcd(c, a)


n = int(input())
data = []

for i in range(0, n):
    A = list(map(int, input().split()))
    data.append(A)
    
for i in range(0, n):
    A = data[i]
    a = min(A)
    b = max(A)
    k = gcd(a, b)
    print(k*(a//k)*(b//k))
    
