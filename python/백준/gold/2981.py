def gcd(a, b):
    p = max(a, b)
    q = min(a, b)
    r = p%q
    if r == 0:
        return q
    else:
        return gcd(q, r)
    
def divisor(k):
    temp = set([])
    for i in range(2, int(k**(1/2)) + 2):
        if k%i == 0:
            temp.add(i)
            temp.add(k//i)
        else:
            pass
    temp.add(k)
    result = list(temp)
    result.sort()
    return result

n = int(input())
data = []
for i in range(0, n):
    a = int(input())
    data.append(a)
    
k = abs(data[0] - data[1])
for i in range(1, n-1):
    difference = abs(data[i] - data[i+1])
    a = gcd(k, difference)
    k = a

result = divisor(k)   
for i in result:
    print(i, end=' ')
