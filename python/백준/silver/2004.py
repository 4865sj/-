def five(n):
    if n//5 == 0:
        return 0
    else:
        k = n//5 + five(n//5)
        return k
    
def two(n):
    if n//2 == 0:
        return 0
    else:
        k = n//2 + two(n//2)
        return k
    
n, r = map(int, input().split())

A = five(n)
a1 = five(r)
a2 = five(n-r)
B = two(n)
b1 = two(r)
b2 = two(n-r)

print(min(A-a1-a2, B-b1-b2))
