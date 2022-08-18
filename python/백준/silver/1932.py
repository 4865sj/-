a = int(input())
A = []
k = int(input())
first = [k]
A.append(first)
for i in range(1, a):
    temp = list(map(int, input().split()))
    A.append(temp)
    
sum = A[0][0]
for i in range(1, a):
    A[i][0] += A[i-1][0]
    A[i][i] += A[i-1][i-1]
    for j in range(1, i):
        if A[i-1][j-1] >= A[i-1][j]:
            A[i][j] += A[i-1][j-1]
        else:
            A[i][j] += A[i-1][j]
            
A[a-1].sort()
print(A[a-1][-1])
