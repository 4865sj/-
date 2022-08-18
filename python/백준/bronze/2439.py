n = int(input())
for i in range(1,n+1):
    a = ''
    for j in range(0, n-i):
        a += ' '
    for k in range(0, i):
        a += '*'
    print(a)
