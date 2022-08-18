n = int(input())
m = 665
count = 0

while True:
    if '666' in str(m):
        count += 1
    else:
        pass
    
    if count == n:
        print(m)
        break
    else:
        m += 1
