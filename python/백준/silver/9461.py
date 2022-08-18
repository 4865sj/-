n = int(input())

temp = [1,1,1,2,2,3]
ans = []
l = 6
for i in range(0, n):
    k = int(input())
    if l < k:
        while l <= k:
            temp.append(temp[l-1]+temp[l-5])
            l += 1
    else:
        pass
    ans.append(temp[k-1])
    
for i in ans:
    print(i)
