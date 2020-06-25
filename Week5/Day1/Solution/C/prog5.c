int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,cnt=0,rem;
	scanf("%d",&num);
	while(num){
		rem = num%10;
		num/=10;
		cnt+=1;
	}
	printf("Count:%d\n",cnt);
}
