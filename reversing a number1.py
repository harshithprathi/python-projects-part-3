n=int(input())
for i in range(n):
    a=int(input())
    b=len(str(a))
    s=0
    for i in range(b):
        c=a%10
        s=s*10+c
        a=a//10
    print(s)
