row = int(input())

a = 64
# Generating pattern
for i in range(1,row+1):
    
    # for space
    for j in range(1, row+1-i):
        print('', end='')
    
    # for increasing pattern
    for j in range(1,i+1):
        print('%c ' %(a+j), end='')
    
    # for decreasing pattern 
    for j in range(i-1,0,-1):
        print('%c ' %(a+j), end='')
    
    # Moving to next line
    print()
