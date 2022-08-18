n = int(input())
result = []

for i in range(0, n):
    a = input()
    result.append(a)
    
for i in range(0, n):
    x = 0
    sum = 0
    k = len(result[i])
    b = result[i]
    for j in range(0, k):
        if b[j] == 'O':
            x += 1
            sum += x
        else:
            x = 0
    print(sum)
            
