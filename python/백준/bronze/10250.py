n = int(input())
ACM = []

for i in range(0, n):
    data = list(map(int, input().split()))
    ACM.append(data)

for i in range(0, n):
    k = ACM[i]
    if k[2]%k[0] == 0:
        y = k[2]//k[0]
    else:
        y = k[2]//k[0] + 1
    x = k[2]%k[0]
    a = k[0]
    if y < 10:
        if x == 0:
            print(str(a), '0', str(y), sep="")
        else:
            print(str(x), '0', str(y), sep="")
    else:
        if x == 0:
            print(str(a), str(y), sep="")
        else:
            print(str(x), str(y), sep="")
