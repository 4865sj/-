n, m = map(int, input().split())
A = []
for i in range(0, n):
    k = int(input())
    if k <= m:
        A.append(k)
    else:
        pass
    
ans = 0
n = len(A)-1
while m != 0:
    temp = m//A[n]
    if temp == 0:
        n -= 1
    else:
        m = m%(temp*A[n])
        ans += temp
        n -= 1
        
print(ans)
