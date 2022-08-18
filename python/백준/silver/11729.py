def from1to3(n):
    if n == 1:
        print(1,3)
    else:
        from1to2(n-1)
        print(1,3)
        from2to3(n-1)
    return

def from2to3(n):
    if n == 1:
        print(2,3)
    else:
        from2to1(n-1)
        print(2,3)
        from1to3(n-1)
    return
        
def from1to2(n):
    if n == 1:
        print(1,2)
    else:
        from1to3(n-1)
        print(1,2)
        from3to2(n-1)
    return
            
def from2to1(n):
    if n == 1:
        print(2,1)
    else:
        from2to3(n-1)
        print(2,1)
        from3to1(n-1)
    return

def from3to1(n):
    if n == 1:
        print(3,1)
    else:
        from3to2(n-1)
        print(3,1)
        from2to1(n-1)
    return

def from3to2(n):
    if n == 1:
        print(3,2)
    else:
        from3to1(n-1)
        print(3,2)
        from1to2(n-1)
    return
            
n = int(input())
print(2**n - 1)
from1to3(n)
