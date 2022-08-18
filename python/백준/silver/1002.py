import math

n = int(input())
data = []
for i in range(0, n):
    position = list(map(int, input().split()))
    data.append(position)
    
for i in range(0, n):
    A = data[i]
    x1, y1, r1, x2, y2, r2 = A[0], A[1], A[2], A[3], A[4], A[5]
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if d == 0 and r1 == r2:
        print(-1)
    else:
        if r1 + r2 == d or abs(r1 - r2) == d:
            print(1)
        elif abs(r1 - r2) > d or abs(r1 + r2) < d:
            print(0)
        else:
            print(2)
