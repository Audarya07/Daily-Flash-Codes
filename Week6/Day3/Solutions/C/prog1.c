int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int a,n,d,sum;
	printf("Starting element: ");
	scanf("%d",&a);
	printf("Number of elements: ");
	scanf("%d",&n);
	printf("Common difference: ");
	scanf("%d",&d);
	sum = a;
	for(int i=0;i<n;i++){
		printf("%d ",sum);
		sum += d;
		if(i!=n-1)
			printf("+ ");
	}
	printf("= %d\n",(n/2)*(2*a+(n-1)*d));
}
