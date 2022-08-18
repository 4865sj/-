A = []
b = 0
n = 1

for i in range(0, 10):
    a = int(input())
    b = a%42
    A.append(b)
    
for i in range(1, 10):
    k = 0
    for j in range(0, i):
        if A[j] == A[i]:
            break
        else:
            k += 1
    if k == i:
        n += 1
        
print(n)
