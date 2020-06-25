int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num1,num2;
	scanf("%d%d",&num1,&num2);
	printf("The minimum amongst %d and %d is ",num1,num2);
	if(num1<num2)
		printf("%d",num1);
	else
		printf("%d",num2);
	printf("\n");
}
