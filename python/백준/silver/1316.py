n = int(input())
A = []
for i in range(0, n):
    a = input()
    A.append(a)
count = 0

for i in range(0, n):
    sample = 0
    a = A[i]
    for j in range(97, 123):
        b = a.count(chr(j))
        if b < 2:
            continue
        else:
            c = a.index(chr(j))
            for k in range(c, b+c):
                if a[k] == chr(j):
                    continue
                else:
                    sample += 1
    if sample == 0:
        count += 1
    else:
        continue
                
                
print(count)
