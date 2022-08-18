result = []
a = 1
b = 1
i = 0
while a != 0 or b != 0:
    a, b = map(int, input().split())
    result.insert(i, a+b)
    i += 1
    
if i > 2:
    for j in range(0,i-1):
        print(result[j])
else:
    print(result[0])
