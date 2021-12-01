a=int(input())
for i in range(a):
	s=input().split()
	x=int(s[0])
	y=int(s[1])
	z=(str(x**y))[::-1]
	print(z[0])



# IN C LANGUAGE
'''#include<stdio.h>
#include<math.h>
int main(){
	int a,i;
	scanf("%d",&a);
	for(i=0;i<a;i++){
		int r,s,x,y,z;
		scanf("%d %d",&r,&s);
		z=pow(r,s);
		printf("%d", z%10);
		printf("\n");
	}
	return 0;
 
}'''
