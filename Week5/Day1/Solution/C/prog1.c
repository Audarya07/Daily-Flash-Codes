int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int n,sum,i,val;
	scanf("%d",&n);
	printf("Abundant numbers:\n");
	for(val=1;val<=n;val++){
		sum=0;
		for(i=1;i<val;i++){
			if(val%i==0)
				sum+=i;
		}
		if(sum>val)
			printf("%d\n",val);
	}
}
