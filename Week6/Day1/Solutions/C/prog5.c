int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,rem,cnt;
	scanf("%d",&num);
	printf("Prime digits in %d are:",num);
	while(num){
		rem=num%10;
		num/=10;
		cnt=0;
		for(int i=1;i<=rem;i++)
			if(rem%i==0)
				cnt+=1;
		if(cnt==2)
			printf("%d ",rem);
	}
	printf("\n");

}
