def test(n):
    z = str(n)
    a, b, c = int(z[0]), int(z[1]), int(z[2])
    if a - b == b - c:
        return 1
    else:
        return 0

k = int(input())

if k<100:
    print(k)
elif 100<= k <1000:
    count = 99
    for i in range(100, k+1):
        count += test(i)
    print(count)
elif k == 1000:
    count = 99
    for i in range(100, 1000):
        count += test(i)
    print(count)
