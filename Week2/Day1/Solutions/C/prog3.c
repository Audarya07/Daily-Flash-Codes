int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int x;
	scanf("%d",&x);
	if(x%2==0)
		printf("%d is Even Number\n",x);
	else
		printf("%d is Odd Number\n",x);
}
