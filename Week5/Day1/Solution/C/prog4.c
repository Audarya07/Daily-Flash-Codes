int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i+j<3)
				printf("  ");
			else if(i+j==3)
				printf("3 ");
			else if(i+j==4)
				printf("%d ",4*j);
			else if(i+j==5)
				printf("%d ",5*j);
			else if(i+j==6)
				printf("%d ",6*j);
		}
		printf("\n");
	}
}
