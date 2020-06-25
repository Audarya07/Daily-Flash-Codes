int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num1,num2;
	scanf("%d%d",&num1,&num2);
	printf("Before swap:num1 = %d snd num2 = %d\n",num1,num2);
	num1 = num1+num2;
	num2 = num1-num2;
	num1 = num1-num2;
	printf("After swap:num1 = %d and num2 = %d\n",num1,num2);
}
