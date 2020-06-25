int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,mul=1,rem;
	scanf("%d",&num);
	while(num){
		rem=num%10;
		num/=10;
		if(rem%2==0)
			mul*=rem;
	}
	printf("Multiplication of even digits: %d\n",mul);
}
