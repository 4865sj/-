m = int(input())
all = []

for i in range(0, m):
    case = list(map(int, input().split()))
    all.append(case)
    
for i in range(0, m):
    case = all[i]
    n = case[0]
    sum = 0
    k = 0
    for j in range(1, n+1):
        sum += case[j]
    mean = sum/n
    for j in range(1, n+1):
        if mean < case[j]:
            k += 1
        else:
            continue
    ratio = (k/n)*100
    print('{0:.3f}%'.format(ratio))
