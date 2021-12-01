n=int(input())
l=[]
for i in range(1,1000):
    if(i%2!=0 and i<=2*n):
        l.append(i)
s=n*2 - 1
for i in l:
        print(int((s-i)/2)*" "  +  i*"*"  +  int((s-i)/2)*" ")
