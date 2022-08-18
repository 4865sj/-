a = int(input())
n = a//5
k = a%5

for i in range(0, n):
    if k%3 == 0:
        print(n + k//3)
        break
    else:
        k += 5
        n += -1
        
if k == a:
    if k%3 == 0:
        print(k//3)
    else:
        print(-1)
else:
    pass
