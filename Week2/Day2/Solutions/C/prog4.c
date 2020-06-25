int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,x;
	scanf("%d",&x);
	for(i=1;i<=10;i++)
		printf("%d ",x*i);
	printf("\n");

}
