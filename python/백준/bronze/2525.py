a, b = map(int, input().split())
c = int(input())
b = b + c

while b >= 60:
    b = b-60
    a += 1
    
if a >= 24:
    a = a-24
    
print(a,b)
