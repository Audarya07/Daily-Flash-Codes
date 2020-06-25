int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,cap=69,small=97;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i>j)
				printf("  ");
			else if(j%2==0){
				printf("%c ",cap);
				cap-=1;
			}
			else if(j%2!=0){
				printf("%c ",small);
				small+=1;
			}
		}
		printf("\n");
	}
}
