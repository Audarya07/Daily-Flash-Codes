int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int val1,val2;
	scanf("%d%d",&val1,&val2);
	printf("Quotient:%d\n",val1/val2);
	printf("Remainder:%d\n",val1%val2);
}
