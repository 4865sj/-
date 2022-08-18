n = int(input())
data = []
for i in range(0, n):
    k = int(input())
    data.append(k)
    
temp = []
out = []
p = 0
q = 0
no = 0

for i in data:
    if i < q:
        p = temp.pop()
        out.append('-')
        if p == i:
            pass
        else:
            no += 1
            break
    else:
        for j in range(0, i-q):
            temp.append(q+j+1)
            out.append('+')
        q = i
        temp.pop()
        out.append('-')
        
if no == 0:
    for j in out:
        print(j)
else:
    print('NO')
