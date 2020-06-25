int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rem=0,base=1;
	printf("Enter Octal number:");
	scanf("%d",&num);
	while(num){
		rem += (num%10)*base;
		num /= 10;
		base *= 8;
	}
	printf("Decimal number:%d\n",rem);
}
