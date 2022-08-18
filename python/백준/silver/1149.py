a = int(input())
A = []
for i in range(0, a):
    temp = list(map(int, input().split()))
    A.append(temp)
    
for i in range(1, a):
    if A[i-1][1] >= A[i-1][2]:
        A[i][0] += A[i-1][2]
    else:
        A[i][0] += A[i-1][1]
    
    if A[i-1][0] >= A[i-1][2]:
        A[i][1] += A[i-1][2]
    else:
        A[i][1] += A[i-1][0]
    
    if A[i-1][0] >= A[i-1][1]:
        A[i][2] += A[i-1][1]
    else:
        A[i][2] += A[i-1][0]
        
A[a-1].sort()
print(A[a-1][0])
