int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,cnt;
	for(i=0;i<4;i++){
		cnt=4;
		for(j=0;j<4;j++){
			if(i+j<3){
				printf("  ");
				cnt--;
			}
			else{
				printf("%c ",cnt+64);
				cnt--;
			}

		}
		printf("\n");
	}
}
