a = input()
b=-1
d='?'

a = a.upper()

for i in range(65, 91):
    c = a.count(chr(i))
    if b < c:
        b = c
        d = chr(i)
    else:
        continue       

for i in range(65, 91):
    if i != ord(d) and b == a.count(chr(i)):
        d = '?'
        break
    else:
        continue
        
print(d)
