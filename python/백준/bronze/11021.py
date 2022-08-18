a = int(input())
result = []
for i in range(0, a):
    b, c = map(int, input().split())
    result.insert(i, b+c) 
    
for i in range(0,a):
    print('Case #'+str(i+1)+':', result[i])
