int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,x,j;
	for(i=0;i<4;i++){
		x=2;
		for(j=0;j<4;j++){
			printf("%d ",x);
			x+=2;
		}
		printf("\n");
	}
}
