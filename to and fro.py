import sys
col=int(raw_input())
while(col!=0):
    string=raw_input()
    row=(len(string))/col
    b=""
    for i in range(0,row):
        if i%2==0:
            b+=string[i*5:(i+1)*5]
        else:
            b+=(string[i*5:(i+1)*5])[::-1]
    c=""
    for k in range(0,col):
        for p in range(0,row):
            c+=b[k+p*col]
    print(c)
    col=int(raw_input())
sys.exit(0)
