a, b = map(int, input().split())
A = set([])
B = set([])

for i in range(1, a+1):
    if a%i == 0:
        A.add(i)
    else:
        pass
    
for i in range(1, b+1):
    if b%i == 0:
        B.add(i)
    else:
        pass
    
C = A & B
k = max(C)
print(k)
print(k*(a//k)*(b//k))
