int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int i,j;
	for(i=0;i<5;i++){
		for(j=0;j<=i;j++){
			if(i%2==0)
				printf("0 ");
			else
				printf("1 ");
		}
	printf("\n");
	}	
}
