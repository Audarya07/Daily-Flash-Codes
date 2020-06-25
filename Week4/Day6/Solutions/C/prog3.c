int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,num,sum;
	for(num=1;num<=100;num++){
		sum=0;
		for(i=1;i<num;i++){
			if(num%i == 0)
				sum+=i;
		}
		if(sum == num)
			continue;
		else
			printf("%d ",num);
	}
	printf("\n");
}

