a, b, c = map(int,input().split())

if (c-a)%(a-b) == 0:
    n = (c-a)//(a-b)
else:
    n = (c-a)//(a-b) + 1

print(n+1)
