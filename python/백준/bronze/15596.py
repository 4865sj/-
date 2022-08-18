def solve(a):
    ans = 0
    n = len(a)
    for i in range(0, n):
        ans += a[i]
    return ans
