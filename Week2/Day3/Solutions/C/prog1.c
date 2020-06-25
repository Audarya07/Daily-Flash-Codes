int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int x,y;
	scanf("%d%d",&x,&y);
	printf("Addition is:%d\n",x+y);
	if(x>y)
		printf("Subtraction is:%d\n",x-y);
	else
		printf("Subtraction is:%d\n",y-x);
}
