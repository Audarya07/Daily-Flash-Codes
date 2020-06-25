int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rem,sum=0i,val;
	scanf("%d",&num);
	val=num;
	while(num){
		rem = num%10;
		num /= 10;
		sum += rem;
	}
	printf("The sum digits from number %d is %d\n",val,sum);
}
