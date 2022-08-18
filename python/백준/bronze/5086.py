data = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        data.append([a,b])

for i in data:
    if i[0] < i[1] and i[1]%i[0] == 0:
        print('factor')
    elif i[0] > i[1] and i[0]%i[1] == 0:
        print('multiple')
    else:
        print('neither')
