import sys

n = int(sys.stdin.readline())
count = [0]*8001
sum = 0

for i in range(n):
    k = int(sys.stdin.readline())
    count[k+4000] += 1
    sum += k
    
data = []
for j in range(0, 8001):
    for k in range(count[j]):
        data.append(j-4000)
    
#산술평균
a = sum/n
print(round(a))

#중앙값
k = n//2
print(data[k])

#최빈값
b = max(count)
c = count.index(b)
d = count.count(b)
if d == 1:
    print(c - 4000)
else:
    for i in range(c+1, 8002):
        if count[i] == b:
            print(i-4000)
            break
        else:
            pass
    
#범위
print(data[n-1] - data[0])
