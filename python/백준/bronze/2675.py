n = int(input())
bundle = []

for i in range(0, n):
    repeat = list(input().split())
    bundle.append(repeat)
    
for i in range(0, n):
    repeat = bundle[i]
    x = repeat[1]
    k = len(x)
    for j in range(0, k):
        for m in range(0, int(repeat[0])):
            print(x[j], end="")
    print()
