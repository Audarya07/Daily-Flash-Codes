int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,a[10];
	for(i=0;i<5;i++)
		scanf("%d",&a[i]);
	printf("Output:\n");
	for(j=i-1;j>=0;j--)
		printf("%d ",a[j]);
	printf("\n");
}
