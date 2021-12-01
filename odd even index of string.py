a=input()
i=0
s=""
r=""
while(i<len(a)):
    if(i==0 or i%2==0):
        s=s+a[i]
    else:
        r=r+a[i]
    i+=1
print(s+" "+r)
    
