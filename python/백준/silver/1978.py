n = int(input())
data = list(map(int, input().split()))
    
m = 0
    
for i in range(0, n):
    k = data[i]
    if k == 1:
        pass
    elif k == 2:
        m += 1
    else:
        for j in range(2, k):
            if k%j == 0:
                break
            else:
                if j == k-1:
                    m += 1
                else:
                    pass                
print(m)
