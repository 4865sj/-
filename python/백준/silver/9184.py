dict = {}

def w(a, b, c):
    if (a,b,c) in dict.keys():
        return dict[(a,b,c)]
    else:
        if a<=0 or b<=0 or c<=0:
            return 1
        elif a>20 or b>20 or c>20:
            return w(20,20,20)
        elif a<b and b<c:
            dict[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a, b-1,c)
            return dict[(a,b,c)]
        else:
            dict[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
            return dict[(a,b,c)]
        
ans = []
while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        ans.append([a,b,c,w(a,b,c)])
for i in ans:
    print('w(',i[0],', ',i[1],', ',i[2],') = ',i[3], sep='')
    
