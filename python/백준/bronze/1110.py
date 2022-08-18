a = int(input())
b = 0
c = a
i = 0
while True:
    b = (c//10) + (c%10)
    c = (c%10) * 10 + (b%10)
    i += 1
    if c != a:
        continue
    else:
        break
        
print(i)
