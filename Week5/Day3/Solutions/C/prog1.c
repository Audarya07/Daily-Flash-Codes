int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,sum;
	scanf("%d",&num);
	for(int i=1;i<=num;i++){
		sum=0;
		for(int j=1;j<i;j++){
			if(i%j==0)
				sum+=j;
		}
		if(sum<i)
			printf("%d ",i);
	}
}
