n = int(input())
data = list(range(1, n+1))
i = 0
j = 0

if n == 1:
    print(1)
else:
    while data[n-2+j]:
        data.append(data[i+1])
        data[i] = 0
        data[i+1] = 0
        i += 2
        j += 1
    
    print(data[n+j-1])
