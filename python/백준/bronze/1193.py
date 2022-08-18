a = int(input())

n = 0
sum = 0

while sum < a:
    n += 1
    sum += n
    
b = sum - a
if n%2 == 0:
    print(n-b, '/', 1+b, sep="")
else:
    print(1+b, '/', n-b, sep="")
