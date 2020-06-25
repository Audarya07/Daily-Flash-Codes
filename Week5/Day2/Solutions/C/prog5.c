int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,cnt=0,rem,val;
	scanf("%d",&num);
	val=num;
	while(num){
		rem = num%10;
		num /= 10;
		if(rem%2==0)
			cnt+=1;
	}
	printf("The number %d has %d even digits\n",val,cnt);
}
