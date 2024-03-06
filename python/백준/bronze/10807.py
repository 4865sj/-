N = int(input())
input1 = list(map(int, input().split()))
a = int(input())

count = 0
for i in range(N):
    if input1[i] == a:
        count += 1
print(count)
