n, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
data.append(0)

sum = 0
i = 0
a = 0
while True:
    sum += (i+1)*(data[i] - data[i+1])
    if k <= sum:
        break
    else:
        i += 1
        
a = (sum - k)//(i+1)
print(data[i+1]+a)
 
