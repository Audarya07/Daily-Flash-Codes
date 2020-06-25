int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,var = 1;
	for(i=0;i<5;i++){
		for(j=0;j<i;j++){
			printf("%d ",var*var);
			var+=1;
		}
	printf("\n");
	}
}
