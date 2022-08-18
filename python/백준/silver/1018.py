m, n = map(int, input().split())
data = []
for i in range(0, m):
    a = input()
    data.append(a)
    
fix = 10000
for i in range(0, m-7):
    for j in range(0, n-7):
        count = 0
        for k in range(0, 8, 2):
            for l in range(0, 8, 2):
                if data[i+k][j+l] != data[i][j]:
                    count += 1
                else:
                    pass
        for k in range(1, 8, 2):
            for l in range(1, 8, 2):
                if data[i+k][j+l] != data[i][j]:
                    count += 1
                else:
                    pass
        for k in range(0, 8, 2):
            for l in range(1, 8, 2):
                if data[i+k][j+l] == data[i][j]:
                    count += 1
                else:
                    pass
        for k in range(1, 8, 2):
            for l in range(0, 8, 2):
                if data[i+k][j+l] == data[i][j]:
                    count += 1
                else:
                    pass
        if count > 32:
            count = 64 - count
        else:
            pass
        if count < fix:
            fix = count
        else:
            pass

print(fix)
