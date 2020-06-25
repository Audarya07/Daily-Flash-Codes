int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int min,max,i;
	printf("\nMin of series:");
	scanf("%d",&min);
	printf("\nMax of series:");
	scanf("%d",&max);
	printf("\nSeries of even numbers ranging between %d and %d is:\n",min,max);
	for(i=min;i<=max;i++)
		if(i%2==0)
			printf("%d ",i);
	printf("\n");

}
