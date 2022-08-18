import sys

n = int(sys.stdin.readline())
a = 1
b = 2

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    i = 2
    while i < n:
        c = (a + b)%15746
        a = b%15746
        b = c%15746
        i += 1
    print(c%15746)
        
        
