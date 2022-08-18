a = int(input())
input1 = []
input2 = []
result = []
for i in range(0, a):
    b, c = map(int, input().split())
    input1.insert(i, b)
    input2.insert(i, c)
    result.insert(i, b+c) 
    
for i in range(0,a):
    print('Case #'+str(i+1)+':', input1[i],'+',input2[i],'=', result[i])
