a=int(input())
b=len(str(a))
s=0
for i in range(0,b):
    n=a%10
    s=s+n
    a=a//10
print(s)


#or

#n=int(input("Enter a number:"))
#tot=0
#while(n>0):
#    dig=n%10
#    tot=tot+dig
#   n=n//10
#print(tot)
