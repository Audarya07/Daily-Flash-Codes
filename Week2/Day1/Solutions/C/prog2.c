int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int x,i,sum=0;
	scanf("%d",&x);
	for(i=0;i<=x;i++)
		sum+=i;
	printf("The sum number upto %d = %d\n",x,sum);
}
