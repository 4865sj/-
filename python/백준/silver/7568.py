n = int(input())
data = []
for i in range(0, n):
    A = list(map(int, input().split()))
    data.append(A)

for i in range(0, n):
    m = 0
    for j in range(0, n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            m += 1
        else:
            pass
    print(m+1, end=" ")
