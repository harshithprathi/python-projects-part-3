def PrefixSuffix(s) :
    l=len(s)     
    for i in range(l//2, 0, -1):
        p=s[0:i]
        q=s[l-i: l]
         
        if(p==q) :
            return i
    return 0
if __name__ == "__main__":
    a=input()
    print(PrefixSuffix(a))
