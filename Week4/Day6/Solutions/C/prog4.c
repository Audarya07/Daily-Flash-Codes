int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,a=0,b=1,c=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i+j<3)
				printf("  ");
			else if(i+j==3)
				printf("= ");
			else{
				c=a+b;
				a=b;
				b=c;
				printf("%d ",a);
			}
		}
		printf("\n");
	}
}

