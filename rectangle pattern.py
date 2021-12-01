lines=int(input())
for i in range(1,lines+1):
    j=lines
    while(j>0):
        if(j!=i):
            print(j,end="")
        else:
            print("*",end="") 
        j-=1
    print()
