a=input()
s=""
for i in a:
    if(i.isupper()):
        s=s+i.lower()
    if(i.islower()):
        s=s+i.upper()
print(s)
