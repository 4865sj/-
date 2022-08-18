n, k = map(int, input().split())
a=1
b=1
i=0
j=0

while i < k:
    a = a*(n-i)
    i += 1
    
while j < k:
    b = b*(k-j)
    j += 1
    
print(a//b)
