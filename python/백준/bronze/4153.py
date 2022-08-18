def tri(a):
    k = 0
    if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        return k
    else:
        m = max(a[0], a[1], a[2])
        sq = []
        for i in range(0, 3):
            if a[i] != m:
                sq.append(a[i])
            else:
                pass
        if m**2 == sq[0]**2 + sq[1]**2:
            k = 1
        else:
            k = 0
        return k

data = []    
while True:
    a = list(map(int, input().split()))
    if a == [0,0,0]:
        break
    else:
        data.append(a)
        
for i in data:
    if tri(i) == 0:
        print('wrong')
    else:
        print('right')
    
