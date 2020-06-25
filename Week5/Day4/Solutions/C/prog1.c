int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,fact,sum=0,rem,val;
	scanf("%d",&num);
	val=num;
	while(num){
		rem = num%10;
		num /= 10;
		fact=1;
		for(int i=1;i<=rem;i++)
			fact*=i;
		sum+=fact;
	}
	if(val==sum)
		printf("%d is Strong number!!\n",val);
	else
		printf("%d is NOT strong number!!\n",val);
}
