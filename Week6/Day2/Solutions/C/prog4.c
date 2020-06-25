int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,cnt;
	for(i=0;i<5;i++){
		cnt=0;
		for(j=0;j<5;j++){
			if(i>j){
				printf("  ");
				cnt+=1;
			}
			else{
				printf("%d ",(i+cnt)*cnt);
				cnt+=1;
			}
		}
		printf("\n");
	}
}
