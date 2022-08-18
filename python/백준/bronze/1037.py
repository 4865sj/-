n = int(input())
data = list(map(int, input().split()))

if n == 1:
    print(data[0]**2)
else:
    a = min(data)
    b = max(data)
    print(a*b)
