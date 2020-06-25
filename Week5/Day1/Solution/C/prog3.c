int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int n,i;
	while(1){
		scanf("%d",&n);
		if(n<0)
			break;
		else
			printf("-->%d\n",n);
	}
}
