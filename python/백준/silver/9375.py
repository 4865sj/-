n = int(input())
data = []

for i in range(0, n):
    m = int(input())
    case = {}
    for j in range(0, m):
        a, b = input().split()
        if b in case.keys():
            case[b].append(a)
        else:
            case[b] = [a]
    data.append(case)
    
for i in range(0, n):
    case = data[i] 
    k = 1
    for j in case.keys():
        k = k*(len(case[j])+1)
    print(k-1)
