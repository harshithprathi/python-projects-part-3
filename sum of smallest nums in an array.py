n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int, input().rstrip().split()))
    x=b[0]
    for i in b:
        if(i<x):
            x=i
    b.remove(x)
    y=b[0]
    for i in b:
        if(i<y):
            y=i
    print(x+y)
            
