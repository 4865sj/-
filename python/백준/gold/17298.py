n = int(input())
data = list(map(int, input().split()))
temp = []

ans = [-1]*n

for i in range(n-1, -1, -1):
    l = len(temp)
    if l == 0:
        temp.append(data[i])
    else:
        while l != 0:
            if temp[l-1] <= data[i]:
                temp.pop()
                l -= 1
            else:
                ans[i] = temp[l-1]
                temp.append(data[i])
                break
        if l == 0 and ans[i] == -1:
            temp.append(data[i])
        else:
            pass
        
for i in ans:
    print(i, end=' ')
                    
