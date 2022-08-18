n = int(input())
data = []

for i in range(0, n):
    a, b = map(int, input().split())
    distance = b-a
    data.append(distance)
    
for i in range(0, n):
    d = data[i]
    k = 0
    sum = 0
    while 2*sum - k <= d:
        k += 1
        sum += k
        
    c = d - 2*(sum - k) + (k-1)
    if c == 0:
        print(2*k - 3)
    elif 0 < c < k:
        print(2*k - 2)
    else:
        print(2*k - 1)
