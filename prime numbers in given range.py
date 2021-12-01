def primeinrange(a,b):
    for i in range(a,b+1):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c+=1
        if(c==2):
            print(i)
n=int(input())
l=[]
for i in range(n):
    st=input().split()
    x=int(st[0])
    y=int(st[1])
    primeinrange(x,y)
       
#OR
'''
n=int(input())
for i in range(n):
    st=input().split()
    x=int(st[0])
    y=int(st[1])
    l= set([r*i for r in range(2,y+1) for i in range(2,y+1)])
    if(x==1):
        res=(sorted(set(range(x+1,y+1))-l))
    else:
        res=(sorted(set(range(x,y+1))-l))
    for i in res:
        print(i)
    
'''
