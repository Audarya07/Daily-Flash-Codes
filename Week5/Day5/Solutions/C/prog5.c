int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rem,cnt=0,val;
	scanf("%d",&num);
	val=num;
	while(num){
		rem=num%10;
		num/=10;
		if(rem==1)
			cnt+=1;
	}
	printf("Number %d has %d Ones\n",val,cnt);
}
