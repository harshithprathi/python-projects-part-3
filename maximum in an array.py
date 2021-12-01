n=int(input())
a=input().split()
x=int(a[0])
for i in a:
    if(int(i)>x):
        x=int(i)
print(x)
