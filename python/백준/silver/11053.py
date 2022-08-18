n = int(input())
seq = list(map(int, input().split()))

dp = [0]*(n+1)
for i in range(0, n):
    m = 1
    for j in range(0, i):
        if seq[j] < seq[i] and dp[j] >= m:
            m = dp[j] + 1
        else:
            pass
    dp[i] = m
  
print(max(dp))
