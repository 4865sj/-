import sys

n = int(sys.stdin.readline())
data = []
k = 0

for i in range(0, n):
    a = sys.stdin.readline()
    if a[0] == 'p':
        if a[1] == 'u':
            data.append(int(a[4:]))
        else:
            if len(data) == k:
                print(-1)
            else:
                print(data[k])
                k += 1
    elif a[0] == 's':
        print(len(data)-k)
    elif a[0] == 'e':
        if len(data) == k:
            print(1)
        else:
            print(0)
    elif a[0] == 'f':
        if len(data) == k:
            print(-1)
        else:
            print(data[k])
    else:
        if len(data) == k:
            print(-1)
        else:
            print(data[-1])
