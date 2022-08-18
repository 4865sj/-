n = int(input())
data = []

for i in range(0, n):
    A = input()
    data.append(A)
    
for i in range(0, n):
    A = data[i]
    l = len(A)
    a = 0
    b = 0
    for j in range(0, l):
        if A[j] == '(':
            a += 1
        else:
            b += 1
            if b > a:
                print('NO')
                break
            else:
                pass
    if a == b:
        print('YES')
    elif a > b:
        print('NO')
    else:
        pass

           
