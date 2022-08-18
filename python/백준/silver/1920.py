n = int(input())
data = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
data_set = set(data)

for i in range(0, m):
    if find[i] in data_set:
        print(1)
    else:
        print(0)
