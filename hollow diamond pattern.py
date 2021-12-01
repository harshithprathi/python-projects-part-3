import math
n=int(input())
for i in range(1,n+1):
    print("Case #"+ str(i)+ ":")
    a = int(input())
    s = math.ceil(a/2)
    for i in range(1, s+1):
        for j in range(1,s-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(s-1,0, -1):
        for j in range(1,s-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
