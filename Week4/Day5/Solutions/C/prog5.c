int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,j;
	for(i=1;i<5;i++){
		for(j=1;j<5;j++){
			if(i==j)
				printf("= ");
			else
				printf("%d",j);
				printf(" ");
		}
		printf("\n");
	}
}
