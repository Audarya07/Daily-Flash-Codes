int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int x,y;
	scanf("%d%d",&x,&y);
	printf("Multiplication is:%d\n",x*y);
	if(x>y)
		printf("Division is:%d\n",x/y);
	else
		printf("Division is:%d\n",y/x);
}
