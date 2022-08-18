n, x = map(int, input().split())
input1 = list(map(int, input().split()))
    
for i in range(0,n):
    if input1[i] < x:
        print(input1[i], end=' ')
