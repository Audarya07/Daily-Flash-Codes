int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int x1,y1,x2,y2;
	int c1,c2,c3;
	printf("Enter number 1:\n");
	printf("\nReal part:");
	scanf("%d",&x1);
	printf("\nImaginery part:");
	scanf("%d",&y1);
	
	printf("Enter number 2:\n");
	printf("\nReal part:");
	scanf("%d",&x2);
	printf("\nImaginery part:");
	scanf("%d",&y2);

	c1 = x1+x2;
	c2 = y1+y2;
	printf("Addition of complex numbers is : %d+%di\n",c1,c2);
}
