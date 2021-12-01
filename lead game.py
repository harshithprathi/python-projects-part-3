'''n=int(input())
l=[]
for i in range(n):
    a=input().split()
    b=int(a[0])-int(a[1])
    l.append(b)
x=max(l)
y=min(l)
if(x>abs(y)):
    print("1",x)
else:
    print("2",abs(y))
'''
n=int(input())
for i in range(n):
    a=int(input())
    i=1
    s=a
    while i<a:
        s=s*i
        i+=1
    print(s)

