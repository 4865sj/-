n = int(input())
k = n
a = n

if k == 1:
    pass
elif k == 2:
    print(2)
else:
    while a != 1:
        k = int(a)
        for i in range(2, k+1):
            if k%i == 0:
                print(i)
                a = k/i
                break
            else:
                pass
                    
