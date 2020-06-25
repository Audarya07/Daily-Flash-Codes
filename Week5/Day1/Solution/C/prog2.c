int printf(const char*,...);
int scanf(const char*,...);

void convert(int oct){
	if(oct>1)
		convert(oct/2);
	printf("%d",oct%2);
}

void main() {
	int oct;
	scanf("%o",&oct);
	printf("Binary equivalent:");
	convert(oct);
	printf("\n");
}
