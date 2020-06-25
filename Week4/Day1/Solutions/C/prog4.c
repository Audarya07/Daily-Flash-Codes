int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,j,k=0;
	for(i=0;i<4;i++){
		k=i;
		for(j=4;j>i;j--){
			printf("%c ",k+65);
			k+=2;
		}
	printf("\n");
	}
}
