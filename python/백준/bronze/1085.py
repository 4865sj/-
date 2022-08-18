x, y, w, h = map(int, input().split())

a = min(x, y, w-x, h-y)
print(a)
