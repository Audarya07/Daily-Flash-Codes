int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,n1,n2,min=0,div=0;
	scanf("%d%d",&n1,&n2);
	if(n1<n2)
		min=n1;
	else
		min=n2;
	for(i=1;i<min;i++)
		if(n1%i==0 && n2%i==0)
			div=i;
	printf("GCD = %d\n",div);
}
