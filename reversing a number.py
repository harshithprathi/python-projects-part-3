a=int(input())
s=0
while(a!=0):
    n=a%10
    s=s*10+n
    a=a//10
print(s)
