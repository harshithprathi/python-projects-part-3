a=input().split()
p=int(a[0])
q=int(a[1])
r=int(a[2])
if(p+q>r and q+r>p and p+r>q):
    print("Yes")
else:
    print("No")
