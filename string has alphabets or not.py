a=input()
count=0
for i in a:
    if(i=="a" or i=="b" or i=="c" or i=="d" or i=="e" or i=="f" or i=="g" or i=="h" or i=="i" or i=="j" or i=="k" or i=="l" or i=="m" or i=="n" or i=="o" or i=="p" or i=="q" or i=="r" or i=="s" or i=="t" or i=="u" or i=="v" or i=="w" or i=="x" or i=="y" or i=="z" or i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" or i=="G" or i=="H" or i=="I" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="O" or i=="P" or i=="Q" or i=="R" or i=="S" or i=="T" or i=="U" or i=="V" or i=="W" or i=="X" or i=="Y" or i=="Z"):
        count+=1
if(count==len(a)):
    print("Yes")
else:
    print("No")
