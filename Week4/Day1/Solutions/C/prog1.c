int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,x,cnt=0;
	scanf("%d",&x);
	for(i=1;i<=x;i++)
		if(x%i==0)
			cnt+=1;
	if(cnt==2)
		printf("%d is prime number\n",x);
	else
		printf("%d is not prime numer\n",x);
}
	
