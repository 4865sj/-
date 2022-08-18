n = int(input())
ans = []

for i in range(0, n):
    a = input()
    k = int(input())
    b = input()
    if b.count(",") == 0:
        if b == '[]':
            data = []
        else:
            data = [int(b[1:-1])]        
    else:
        data = list(map(int, b[1:-1].split(",")))
    p = a.count('D')
    if p > k:
        ans.append('error')
    else:
        l = len(a)
        i = 0
        for j in range(0, l):
            if a[j] == 'R':
                if i == 0:
                    i = 1
                else:
                    i = 0
            else:
                if i == 0:
                    data.remove(data[0])
                else:
                    data.pop()
        if i == 1:
            data.reverse()
        else:
            pass
        ans.append(data)
        
for i in ans:
    if i == 'error':
        print(i)
    else:
        print('[', end='')
        l = len(i)
        for j in range(0, l):
            print(i[j], sep='', end='')
            if j != l-1:
                print(',', end='')
            else:
                print(']')
        if l == 0:
            print(']')
        else:
            pass
    
