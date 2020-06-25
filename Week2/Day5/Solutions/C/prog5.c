int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int i,num;
	scanf("%d",&num);
	printf("Perfect divisors of %d are:",num);
	for(i=1;i<num;i++)
		if(num%i==0)
			printf("%d ",i);	
printf("\n");
}
