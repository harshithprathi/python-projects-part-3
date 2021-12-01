a=int(input())
s=a
c=0
while(s>0):
    n=s%10
    c=c+n**4
    s=s//10
if(a==c):
    print("Yes")
else:
    print("No")
    
    #or
'''def countDigit(n) :
    if (n == 0) :
        return 0
 
    return (1 + countDigit(n // 10))
     
 
def check(n) :
     
    l = countDigit(n)
    dp = n; sum = 0
 
    while (dp) :
        sum = sum + pow(dp % 10, l)
        dp = dp // 10
     
    return (n == sum)
     
 
n = int(input())
if (check(n)) :
    print( "Yes")
else :
    print( "No")
     
     '''
