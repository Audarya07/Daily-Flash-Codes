int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i+j<3)
				printf("   ");
			else{
				printf("%c%d ",68-j,i+j);
			}

		}
		printf("\n");
	}
}
