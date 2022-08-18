def five(n):
    if n//5 == 0:
        return 0
    else:
        k = n//5 + five(n//5)
        return k

n = int(input())
print(five(n))
