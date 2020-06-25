int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i;
	for(i=1;i<=100;i++){
		if(i%7==0)
			continue;
		else
			printf("%d ",i);

	}
	printf("\n");
}
