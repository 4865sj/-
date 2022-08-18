a = int(input())

dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (a+2)
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, a+1):
  temp  = [0]*10
  temp[0] = dp[i-1][1]
  temp[9] = dp[i-1][8]
  for j in range(1, 9):
    temp[j] = dp[i-1][j-1] + dp[i-1][j+1]
  dp[i] = temp
        
ans = 0
for i in range(0, 10):
    ans += dp[a][i]
       
print(ans%1000000000)
