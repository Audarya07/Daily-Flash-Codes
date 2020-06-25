int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,x,num=9,sum=0;
	scanf("%d",&x);
	for(i=0;i<x;i++){
		sum+=num;
		num = num*10+9;
	}
	printf("Sum = %d\n",sum);
}
