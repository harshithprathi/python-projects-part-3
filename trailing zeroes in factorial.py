t=int(input())
for i in range(t):
    a=int(input())
    def findTrailingZeros(n):
        count = 0
        while(n >= 5):
            n //= 5
            count += n
        return count
    print(findTrailingZeros(a))
    
