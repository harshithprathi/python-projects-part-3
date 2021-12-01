n=int(input())
for i in range(n):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    s=0
    for i in range(1,x+1):
        if(x%i==0 and y%i==0):
            s=i
    print(s,end=" ")
    print(int(x/s)*y)
    
# GCD = greatest common divisor
# LCM = (x/GCD)*y
