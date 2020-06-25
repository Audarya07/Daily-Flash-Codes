int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num;
	scanf("%d",&num);
	while(num>=0){
		if(num%2==0)
			printf("%d ",num);
		num-=1;
	}
	printf("\n");
}
