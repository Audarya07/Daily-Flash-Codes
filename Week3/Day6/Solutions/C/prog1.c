int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,n;
	scanf("%d",&n);
	for(i=n;i>0;i--){
		if(i%2!=0)
			printf("%d ",i);
	}
}
