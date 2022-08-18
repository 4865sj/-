n = input()
l = len(n)
data = []

for i in range(0, l):
    data.append(int(n[i]))
    
data.sort(reverse=True)

for i in range(0, l):
  data[i] = str(data[i])


k = ''.join(data)
    
print(k)
