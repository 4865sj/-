n, k = map(int, input().split())

data = list(range(1, n+1))
ans = []
p = 0

while len(ans) != n:
    for i in range(0, k-1):
        a = data[p+i]
        data.append(a)
        data[p+i]=0
    p += k-1
    l = len(data)
    if data[p] != 0 and p < l:
        ans.append(data[p])
        data[p] = 0
        p += 1
    else:
        break
        
print('<', end='')
for i in range(0, n):
    print(ans[i], end='')
    if i != n-1:
        print(', ', end='')
    else:
        print('>')
    
