n, m = map(int, input().split())
data = list(map(int, input().split()))
seq = list(range(1, n+1)) + [0]*50000
initial = 0
terminal = n-1
ans = 0

for i in data:
    if seq[initial] == i:
        seq[initial] = 0
        initial += 1
    else:
        a = seq.index(i)
        if a - initial <= terminal - a + 1:
            ans += a - initial
        else:
            ans += terminal - a + 1
        for i in range(0, a - initial):
            seq[terminal + 1 + i] = seq[initial + i]
            seq[initial + i] = 0
        terminal += a-initial
        initial = a+1
print(ans)
