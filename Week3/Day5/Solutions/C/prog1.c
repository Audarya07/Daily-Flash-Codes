int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,i,sum=0,j=1;
	scanf("%d",&num);
	for(i=1;i<10;i++){
		printf("%d ",j);
		j+=num;	
	}
	printf("\n");
}
