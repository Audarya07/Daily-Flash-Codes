int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,i,sum,val;
	scanf("%d",&num);
	for(val=1;val<num;val++){
		sum=0;
		for(i=1;i<val;i++){
			if(val%i==0)
				sum+=i;
		}
	if(sum==val)
		printf("%d ",val);
	}
}

