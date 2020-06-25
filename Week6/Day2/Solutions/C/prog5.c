int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rem,val;
	scanf("%d",&num);
	val=num;
	printf("The perfect divisor digits of %d are :",val);
	while(num){
		rem = num%10;
		num/=10;
		if(val%rem==0)
			printf("%d ",rem);
	}
	printf("\n");
}
