import sys
n = int(sys.stdin.readline())
count = [0]*10001 

for i in range(0, n):
    count[int(sys.stdin.readline())] += 1   

for i in range(1, 10001):
    for j in range(0, count[i]):
        print(i)  
