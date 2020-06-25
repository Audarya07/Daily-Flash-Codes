int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j;
	for(i=0;i<4;i++){
		for(j=4;j>i;j--){
			if(j%2==0)
				printf("+ ");
			else
				printf("= ");
		}
		printf("\n");
	}
}
