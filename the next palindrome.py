n=int(input())
for i in range(n):
	a=int(input())
	s=a
	for i in range(1000000000000):
		s+=1
		if(str(s)==str(s)[::-1]):
			print(s)
			break
		
