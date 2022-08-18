def func(a):
    if 65 <= a <= 67:
        return 3
    elif 68 <= a <= 70:
        return 4
    elif 71 <= a <= 73:
        return 5
    elif 74 <= a <= 76:
        return 6
    elif 77 <= a <= 79:
        return 7
    elif 80 <= a <= 83:
        return 8
    elif 84 <= a <= 86:
        return 9
    elif 87 <= a <= 90:
        return 10
    
a = input()
b = len(a)
sum = 0

for i in range(0, b):
    sum += func(ord(a[i]))
    
print(sum)
