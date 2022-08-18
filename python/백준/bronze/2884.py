a, b = map(int, input().split())
if b - 45 < 0:
    b = b + 15
    a = a - 1
else:
    b = b - 45
    
if a == -1:
    a = 23

print(a, b)
