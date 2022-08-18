a = int(input())
A = []
for i in range(0, a):
    temp = int(input())
    A.append(temp)

if a == 1:
    print(A[0])
elif a == 2:
    print(A[0]+A[1])
else:
    dp = [0]*a
    dp[0] = A[0]
    dp[1] = A[0] + A[1]
    dp[2] = max(A[0]+A[2], A[1]+A[2])

    for i in range(3, a):
        dp[i] = max(dp[i-3] + A[i-1] + A[i], dp[i-2] + A[i])
    
    print(dp[a-1])

    
