int printf(const char*,...);
int scanf(const char*,...);
#include<math.h>

void main() {
	int num,val1,rem,length=0;
	int val;
	scanf("%d",&num);
	val1=num;	
	val=num;
	printf("Quotient of divisions are:\n");
	while(num){
		length+=1;
		num/=10;
	}
	while(val){
		rem=val/pow(10,length-1);
		val=val%(int)pow(10,length-1);
		length-=1;
		printf("%d/%d = %d\n",val1,rem,val1/rem);
	}
}
