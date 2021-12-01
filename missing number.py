def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return int(total - sum_of_A)
n=int(input())
for i in range(n):
    a=int(input())
    b=sorted(list(map(int, input().split())))
    x=getMissingNo(b)
    print(x)
            
    
