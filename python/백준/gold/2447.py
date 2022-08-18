def star(n):
    if n == 3:
        draw[0][:2] = draw[2][:2] = ['*']*3
        draw[1][:2] = ['*',' ','*']
        return
    else:
        k = n//3
        star(k)
        for i in range(0, k):
            for j in range(0, k):
                draw[i+k][j] = draw[i+2*k][j] = draw[i][j+k] = draw[i+2*k][j+k] = draw[i][j+2*k] = draw[i+k][j+2*k] = draw[i+2*k][j+2*k] = draw[i][j]
                    
n = int(input())
draw = [[' ' for i in range(n)] for j in range(n)]
star(n)

for i in range(0, n):
    for j in range(0, n):
        print(draw[i][j], end="")
    print()
