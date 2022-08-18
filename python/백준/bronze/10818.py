n = int(input())
input1 = list(map(int, input().split()))

input1.sort()
print(input1[0], input1[n-1])
