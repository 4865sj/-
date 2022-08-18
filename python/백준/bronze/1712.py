a, b, c = map(int, input().split())
n = 1

if b >= c:
    print(-1)
else:
    n = a//(c-b)
    print(n+1)
