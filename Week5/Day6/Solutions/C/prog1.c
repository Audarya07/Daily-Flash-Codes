int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,i,cnt=0,rem;;
	scanf("%d",&num);
	printf("Prime numbers are :");
	while(num){
		rem=num%10;
		num/=10;
		cnt=0;
		for(i=1;i<=rem;i++){
			if(rem%i==0)
				cnt+=1;
		}
		if(cnt==2)
			printf("%d ",rem);
		
	}
	printf("\n");
}
