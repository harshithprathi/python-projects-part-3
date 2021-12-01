def reverseBits(num,bitSize): 
    
     # convert number into binary representation 
     # output will be like bin(10) = '0b10101' 
     binary = bin(num) 
    
     # skip first two characters of binary 
     # representation string and reverse 
     # remaining string and then append zeros 
     # after it. binary[-1:1:-1]  --> start 
     # from last character and reverse it until 
     # second last character from left 
     reverse = binary[-1:1:-1] 
     reverse = reverse + (bitSize - len(reverse))*'0'
    
     # converts reversed binary string into integer 
     print (int(reverse,2)) 
    
# Driver program 
if __name__ == "__main__": 
    num = int(input())
    bitSize = 32
    reverseBits(num,bitSize)
