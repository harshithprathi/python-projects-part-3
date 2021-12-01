t=int(input())
while t>0:
    k=int(input())
    rev=0
    while k!=rev:
        k=k+1
        no=k
        rev=0
        while no>0:
            rev=(rev*10)+(no%10)
            no=no//10
        if k==rev:
            print(k)
    t=t-1
