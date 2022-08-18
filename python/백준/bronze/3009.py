x_list = []
y_list = []
for i in range(0,3):
    position = list(map(int,input().split()))
    x_list.append(position[0])
    y_list.append(position[1])
    
if x_list[0] == x_list[1]:
    x = x_list[2]
elif x_list[0] == x_list[2]:
    x = x_list[1]
else:
    x = x_list[0]
    
if y_list[0] == y_list[1]:
    y = y_list[2]
elif y_list[0] == y_list[2]:
    y = y_list[1]
else:
    y = y_list[0]
    
print(x, y)
    
