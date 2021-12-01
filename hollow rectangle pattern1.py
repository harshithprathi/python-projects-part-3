a=int(input())
b=int(input())
for i in range(b):
    for j in range(a):
        if(i==0 or i==b-1 or j==0 or j==a-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
