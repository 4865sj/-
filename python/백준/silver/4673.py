def sum(n):
    k = len(str(n))
    ans = n
    for i in range(0, k):
        ans += int(str(n)[i])
    return ans


a = list(range(1, 10001))
not_self = []

for i in range(1, 10000):
    j = sum(i)
    if j <= 10000:
        not_self.append(j)
    else:
        continue

not_self_set = set(not_self)        
new_list = list(not_self_set)

for i in new_list:
    a.remove(i)
    
b = len(a)
for i in range(0, b):
    print(a[i])
