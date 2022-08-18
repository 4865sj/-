import sys

a = int(input())
result = []
for i in range(0, a):
    b, c = map(int, sys.stdin.readline().split())
    result.insert(i, b+c) 
    
for i in range(0,a):
    print(result[i])
