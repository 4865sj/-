n = int(input())
data = []
ans = []

for i in range(0, n):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    j = 0
    while A[b] != 0:
        m = max(A)
        while True:
            if A[j] == m:
                A[j] = 0
                i += 1
                break
            else:
                j += 1
                if j == a:
                    j = 0
                else:
                    pass
    ans.append(i)
    
for i in ans:
    print(i)
