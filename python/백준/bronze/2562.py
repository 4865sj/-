inputs = []
k = 0

for i in range(0, 9):
    a = int(input())
    inputs.append(a)
    
max = sorted(inputs)
m = max[8]

for i in range(0, 9):
    if inputs[i] == m:
        k = i
        break
    else:
        continue
        
print(m)
print(k+1)
