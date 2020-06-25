int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,x=7;
	for(i=0;i<4;i++){
		for(j=0;j<=i;j++){
			printf("%d ",x);
			x-=1;
		}
	x+=1;
	printf("\n");
	}
}
