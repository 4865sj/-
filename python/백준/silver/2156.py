n = int(input())
A = []
for i in range(0, n):
    k = int(input())
    A.append(k)

if n == 1:
    print(A[0])
elif n == 2:
    print(A[0] + A[1])
else:
    dp = [0]*n
    dp[0] = A[0]
    dp[1] = A[0] + A[1]
    dp[2] = max(A[0]+A[2], A[1]+A[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + A[i-1] + A[i], dp[i-2] + A[i], dp[i-1])
    print(max(dp[-1], dp[-2]))
