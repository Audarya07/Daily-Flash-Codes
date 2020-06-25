int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,val;
	scanf("%d",&num);
	val=num;
	while(num>=0){
		if(num%2!=0)
			printf("%d ",num);

		num-=1;
	}
}
