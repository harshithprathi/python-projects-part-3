n=int(input())
for i in range(n):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    z=int(a[2])
    b=x
    for i in a:
        if(int(i)>b):
            b=int(i)
    a.remove(str(b))
    c=int(a[0])
    for i in a:
        if(int(i)>c):
            c=int(i)
    print(c)
        
        
            
