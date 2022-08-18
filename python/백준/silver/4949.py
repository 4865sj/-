data = []
while True:
    n = input()
    if n == '.':
        break
    else:
        data.append(n)
        

for x in data:
    l = len(x)
    a=0
    b=0
    c=0
    d=0
    a_index = []
    c_index = []
    check = 0
    for i in range(0, l):
        if x[i] == '(':
            a += 1
            a_index.append(i)
        elif x[i] == ')':
            b += 1
            k = len(a_index)
            if k == 0:
                pass
            else:
                temp = x[a_index[k-1]:i]
                if temp.count('[') != temp.count(']'):
                    print('no')
                    check += 1
                    break
                else:
                    pass
                a_index.remove(a_index[k-1])

        elif x[i] == '[':
            c += 1
            c_index.append(i)
        elif x[i] == ']':
            d += 1
            k = len(c_index)
            if k == 0:
                pass
            else:
                temp = x[c_index[k-1]:i]
                if temp.count('(') != temp.count(')'):
                    print('no')
                    check += 1
                    break
                else:
                    pass
                c_index.remove(c_index[k-1])
        else:
            pass
        
        if a < b or c < d:
            print('no')
            break
        else:
            pass
    
    if check == 1:
        pass
    else:
        if a == b and c == d:
            print('yes')
        elif a < b or c < d:
            pass
        else:
            print('no')
        
