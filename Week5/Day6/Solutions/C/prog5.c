int printf(const char*,...);
int scanf(const char*,...);
#include<math.h>

void main() {
	int num,val,cnt,rem,rem1,length=0;
	
	scanf("%d",&num);
	val=num;
	while(num){
		rem=num%10;
		num/=10;
		length+=1;
	}
	
	while(val){
		rem1=val/(int)pow(10,length-1);
		val = val%(int)pow(10,length-1);
		length-=1;
		int fact=1;
		for(int i=1;i<=rem1;i++)
			fact*=i;
		printf("Factorial of %d is %d\n",rem1,fact);
	}
}
