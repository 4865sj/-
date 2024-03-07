a, b = map(int, input().split())
M = 0
m = 0
if a > b:
    M = a
    m = b
else:
    M = b
    m = a

result = M*m

while m != 0:
    r = M%m
    M = m
    m = r

print(result//M)
