int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,num=10;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i+j<3)
				printf("  ");
			else{
				printf("%d ",num*num);
				num-=1;
			}
		}
		printf("\n");
	}
}
