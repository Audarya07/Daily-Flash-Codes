int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,sum=0;
	for(i=1;i<=10;i++)
		sum+=i;
	printf("Sum of first 10 natural numbers = %d\n",sum);
}
