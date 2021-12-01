def isnthbitset(n,bt):
    if n& (1 << bt):
        print("true")
    else:
        print("false")
a=input().split()
n=int(a[0])
bt=int(a[1])
isnthbitset(n,bt)
