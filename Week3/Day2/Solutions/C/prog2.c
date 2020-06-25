int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num1,num2,i,j,fact;
	scanf("%d %d",&num1,&num2);
	for(i=num1;i<=num2;i++){
		fact = 1;
		for(j=1;j<=i;j++){
			fact*=j;
		}
	printf("Factorial of %d is : %d\n",i,fact);
	}
}
