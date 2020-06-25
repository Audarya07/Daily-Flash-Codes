int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rev=0;
	scanf("%d",&num);
	while(num){
		rev = (rev*10) + (num%10);
		num /= 10;
	}
	printf("Reverse:%d\n",rev);
}
