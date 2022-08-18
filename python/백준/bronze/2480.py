A = list(map(int, input().split()))
A_set = set(A)
A_list = list(A_set)

if len(A_list) == 1:
    print(10000 + A[0]*1000)
elif len(A_list) == 2:
    if A.count(A_list[0]) == 2:
        print(1000+A_list[0]*100)
    else:
        print(1000+A_list[1]*100)
else:
    A.sort()
    print(A[-1]*100)
