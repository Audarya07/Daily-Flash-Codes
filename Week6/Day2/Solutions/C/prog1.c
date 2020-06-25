int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int a,n,d,sum;
	printf("Starting element:");
	scanf("%d",&a);
	printf("Number of elements:");
	scanf("%d",&n);
	printf("Common difference:");
	scanf("%d",&d);
	sum=a;
	for(int i=1;i<=n;i++){
		printf("%d ",sum);
		sum+=d;
	}
	printf("\n");
}
