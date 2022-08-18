import sys

n = int(input())
data = []

for i in range(0, n):
    a = sys.stdin.readline()
    if a[0] == 'p':
        if a[1] == 'u':
            data.append(int(a[4:]))
        else:
            l = len(data)
            if l == 0:
                print(-1)
            else:
                print(data[l-1])
                data.pop()
    elif a[0] == 's':
        print(len(data))
    elif a[0] == 'e':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    else:
        l = len(data)
        if l == 0:
            print(-1)
        else:
            print(data[l-1])
