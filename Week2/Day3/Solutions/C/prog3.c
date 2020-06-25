int printf(const char*,...);
int scanf(const char *,...);
#include<math.h>
void main() {
	int x,y,a1,a2,b1,b2;
	scanf("%d%d",&x,&y);
	a1=pow(x,3);
	a2=pow(y,3);
	b1=pow(x,2);
	b2=pow(y,2);
	printf("Addition of %d & %d is:%d\n",a1,a2,a1+a2);
	printf("Subtraction of %d & %d is:%d\n",b1,b2,b1-b2);
}
