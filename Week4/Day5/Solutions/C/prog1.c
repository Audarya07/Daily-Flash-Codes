int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int x,cnt=0;
	scanf("%d",&x);
	for(int i=1;i<=x;i++)
		if(x%i==0)
			cnt+=1;
	if(cnt==2)
		printf("It is Prime!!\n");
	else
		printf("Not Prime!!\n");
}
