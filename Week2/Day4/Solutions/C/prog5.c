int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int i,fact=1,x;
	scanf("%d",&x);
	for(i=1;i<=x;i++)
		fact*=i;
	printf("Factorial is : %d\n",fact);	
}
