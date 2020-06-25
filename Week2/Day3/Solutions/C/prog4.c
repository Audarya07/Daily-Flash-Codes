int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int x,y;
	char c;
	printf("\nEnter first number:");
	scanf("%d",&x);
	printf("\nEnter second number:");
	scanf("%d",&y);
	printf("\nEnter sign of operation:");
	scanf(" %c",&c);

	if(c=='+')
		printf("Addition is:%d\n",x+y);
	else if(c=='-')
		printf("Subtraction is:%d\n",x-y);
	else if(c=='*')
		printf("Multiplication is:%d\n",x*y);
	else if(c=='/')
		printf("Division is:%d\n",x/y);
}
