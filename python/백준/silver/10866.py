import sys

n = int(sys.stdin.readline())
data = []

for i in range(0, n):
    a = sys.stdin.readline()
    if a[0] == 'p':
        if a[1] == 'u':
            if a[5] == 'f':
                data = [int(a[11:])] + data
            else:
                data.append(int(a[10:]))
        else:
            if a[4] == 'f':
                if len(data) != 0:
                    print(data[0])
                    data.remove(data[0])
                else:
                    print(-1)
            else:
                if len(data) != 0:
                    print(data[-1])
                    data.pop()
                else:
                    print(-1)
    elif a[0] == 's':
        print(len(data))
    elif a[0] == 'e':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'f':
        if len(data) != 0:
            print(data[0])
        else:
            print(-1)
    elif a[0] == 'b':
        if len(data) != 0:
            print(data[-1])
        else:
            print(-1)
    else:
        pass
