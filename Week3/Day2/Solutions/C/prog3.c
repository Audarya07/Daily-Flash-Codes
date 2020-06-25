int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int r,i;
	printf("\nI = ");
	scanf("%d",&i);
	printf("\nR = ");
	scanf("%d",&r);
	printf("\nVoltage V = %d\n",i*r);
}
