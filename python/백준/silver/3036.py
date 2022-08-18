def gcd(a, b):
    p = max(a, b)
    q = min(a, b)
    r = p%q
    if r == 0:
        return q
    else:
        return gcd(q, r)

n = int(input())
data = list(map(int, input().split()))

k = data[0]
for i in range(1, n):
    print(data[0]//gcd(data[0], data[i]), '/', data[i]//gcd(data[0], data[i]), sep='')
