n = int(input())
data = []

for i in range(0, n):
    a = int(input())
    if a == 0:
        data.pop()
    else:
        data.append(a)

sum = 0
for i in data:
    sum += i
print(sum)
