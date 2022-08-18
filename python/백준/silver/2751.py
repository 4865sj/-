import sys

def merge(left, right):
    i = j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        result = result + right[j:len(right)]
    elif j == len(right):
        result = result + left[i:len(left)]
    else:
        pass
    return result

def cut(data):
    l = len(data)//2
    left = data[0:l]
    right = data[l:len(data)]
    if len(left) > 2:
        left = cut(left)
    elif len(left) == 2:
        if left[0] > left[1]:
            left.reverse()
        else:
            pass
    else:
        pass
    
    if len(right) > 2:
        right = cut(right)
    elif len(right) == 2:
        if right[0] > right[1]:
            right.reverse()
        else:
            pass
    else:
        pass
    return merge(left, right)

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(int(sys.stdin.readline()))
    
result = cut(data)
for i in range(n):
    print(result[i])
