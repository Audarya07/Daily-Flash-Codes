int printf(const char*,...);
int scanf(const char*,...);
#include<math.h>
void main() {
	int num,i,sum=0,sum1=0;
	scanf("%d",&num);
	int a[num];
	for(i=0;i<num;i++){
		sum+=pow(10,i);
		a[i] = sum;
		sum1+=a[i];
	}
	printf("The sum is %d\n",sum1);
}
