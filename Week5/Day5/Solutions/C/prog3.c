int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,avg,cnt=0,rem,val,sum=0;
	scanf("%d",&num);
	val=num;
	while(num){
		rem=num%10;
		num/=10;
		sum+=rem;
		cnt+=1;
	}
	printf("Average of digits of %d is %d\n",val,sum/cnt);
}
