n = int(input())
for i in range(1,n+1):
    k=0
    for j in range(1,n-i+1):
        print(" ", end="")
    while(k!=2*i-1):
        print("*", end="")
        k=k+1
    print()
