n=int(input())
c=0
for i in range(1, int(n**0.5)+1):
	for j in range(i+1, (i*j)+1):
		c+=1
	c+=int(n**0.5)
	print(c)
