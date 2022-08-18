n = int(input())
score = list(map(int, input().split()))
sum = 0
score.sort()
max = score[n-1]

for i in range(0, n):
    k = (score[i]/max)*100
    sum += k
       
mean = sum/n
print(mean)
    
