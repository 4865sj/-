a, b = map(int, input().split())
data = []
sum = 0

for i in range(0, a):
    k = int(input())
    data.append(k)
    sum += k
    
initial = 1
terminal = sum//b + 1

while True:
    mid = (initial + terminal)//2
    k = 0
    l = 0
    for i in range(0, a):
        k += data[i]//mid
        l += data[i]//(mid + 1)
    
    if k == b:
        if l < b:
            print(mid)
            break
        else:
            initial = mid
    elif k < b:
        terminal = mid
    else:
        if l < b:
            print(mid)
            break
        else:
            initial = mid
            
