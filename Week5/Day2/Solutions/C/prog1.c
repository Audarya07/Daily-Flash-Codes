int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,i,sum=0;
	scanf("%d",&num);
	for(i=1;i<num;i++)
		if(num%i==0)
			sum+=i;
	if(sum<num)
		printf("%d is deficient number!!\n",num);
	else
		printf("%d is NOT deficient number!!\n",num);
}
