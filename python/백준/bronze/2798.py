n, m = map(int,input().split())
data = list(map(int,input().split()))
sum = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if sum < data[i] + data[j] + data[k] <= m:
                sum = data[i] + data[j] + data[k]
                
print(sum)
