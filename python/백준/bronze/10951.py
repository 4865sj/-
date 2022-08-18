i = 0
result = []
while True:
    try:
        a, b = map(int, input().split())
        result.insert(i, a+b)
        i += 1
    except EOFError:
        break

for j in range(0, i):
    print(result[j])
