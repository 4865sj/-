import sys

n = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))
count = [0]*20000001

for x in cards:
    count[x+10000000] += 1
    
m = int(sys.stdin.readline())

find = list(map(int, sys.stdin.readline().split()))
    
for i in range(0, m):
    print(count[find[i]+10000000], end=" ")
