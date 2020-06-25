int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rem,cnt=0,sum=0;
	scanf("%d",&num);
	while(num){
		rem = num%10;
		num/=10;
		cnt+=1;
		sum+=rem;
	}
	printf("Sum of digits:%d\n",sum);
	printf("Average of sum of digits:%d\n",sum/cnt);
}
