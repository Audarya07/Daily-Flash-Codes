int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,i,sum=0;
	scanf("%d",&num);
	for(i=1;i<num;i++)
		if(num%i==0)
			sum+=i;
	if(sum==num)
		printf("%d is Perfect number\n",num);
	else
		printf("%d is not perfect number\n",num);
}
