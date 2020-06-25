int printf(const char*,...);
int scanf(const char*,...);
#include<math.h>

void main() {
	int num,rem,a[5],i,val,val1,length=0;
	scanf("%d",&num);
	val1 = num;
	while(val1){
		length+=1;
		val1/=10;
	}
	while(num){
		rem = num/pow(10,length-1);
		num %= (int)pow(10,length-1);
		length-=1;
		i=0;
		val=rem;
		while(rem){
			a[i]=rem%2;
			rem/=2;
			i++;
		}
		printf("Binary of %d: ",val);
		for(int j=i-1;j>=0;j--)
			printf("%d",a[j]);
		printf("\n");
	}
}
