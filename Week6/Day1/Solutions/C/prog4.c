int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,num;
	for(i=0;i<5;i++){
		num=5;
		for(j=0;j<5;j++){
			if(i>j)
				printf("  ");
			else
				printf("%d ",num);
			num-=1;
		}
		printf("\n");
	}
}
