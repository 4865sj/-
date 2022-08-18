m = int(input())
n = int(input())
k = 0
sum = 0

for i in range(n, m-1, -1):
    for j in range(2, i):
        if i%j == 0:
            break
        else:
            if j == i-1:
                k = i
                sum += k
            else:
                pass

if m == 1 and n != 1:
    k = 2
    sum += k
elif m == 2:
    k = 2
    sum += k
else:
    pass

if sum == 0:
    print(-1)
else:
    print(sum)
    print(k)  
