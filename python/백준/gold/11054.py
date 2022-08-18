n = int(input())
seq = list(map(int, input().split()))

dp1 = [0]*(n+1)
dp2 = [0]*(n+1)
dp3 = [0]*(n+1)

for i in range(0, n):
    m = 1
    for j in range(0, i):
        if seq[j] < seq[i] and dp1[j] >= m:
            m = dp1[j] + 1
        else:
            pass
    dp1[i] = m
    
for i in range(0, n):
    m = 1
    for j in range(0, i):
        if seq[n-j-1] < seq[n-i-1] and dp2[n-j-1] >= m:
            m = dp2[n-j-1] + 1
        else:
            pass
    dp2[n-i-1] = m
    
for i in range(0, n):
    dp3[i] = dp1[i] + dp2[i]
    
print(max(dp3)-1)
    
