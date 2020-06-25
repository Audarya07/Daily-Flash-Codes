int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int r;
	printf("Enter radius: ");
	scanf("%d",&r);
	printf("Circumference of circle: %.2f\n",2*3.142*r);
}
