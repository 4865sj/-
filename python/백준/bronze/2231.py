n = int(input())
m=0

for i in range(1, n):
    k = str(i)
    l = len(k)
    sum = i
    for j in range(0, l):
        sum += int(k[j])
    if sum == n:
        m = i
        break
    else:
        continue

print(m)
