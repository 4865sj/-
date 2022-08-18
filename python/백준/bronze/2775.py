a = int(input())
A = []
for i in range(0, a):
    k = int(input())
    n = int(input())
    A.append([k,n])
    
for i in range(0, a):
    room = A[i]
    k = room[0]
    n = room[1]
    previous = list(range(1, n+1))
    after = list(range(1, n+1))
    for j in range(0, k):
        sum = 0
        for l in range(0, n):
            sum += previous[l]
            after[l] = sum
        previous = after
    print(after[n-1])
