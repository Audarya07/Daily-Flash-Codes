int printf(const char*,...);
int scanf(const char *,...);

void main() {
	int i;
	for(i=1;i<=100;i++)
		if(i%4==0 && i%7==0)
			printf("%d ",i);
	printf("\n");
}
