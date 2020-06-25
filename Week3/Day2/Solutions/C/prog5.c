int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num1,num2,num3,min;
	scanf("%d%d%d",&num1,&num2,&num3);
	
	if(num1<num2 && num1<num3)
		min=num1;
	else if(num2 < num3)
	        min = num2;
	else
        	min = num3;
	printf("Minimum amongst %d,%d and %d is:%d\n",num1,num2,num3,min);
}
