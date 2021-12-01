r=int(input()) 
k=1
for i in range(1,r+1):
    d=r-1
    val=i
    for j in range(1,i+1):  
        print(val,end=" ")
        val+=d
        d=d-1
        k+=1 
    print("                                                                         ")
