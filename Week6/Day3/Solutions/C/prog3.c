int printf(const char*,...);
int scanf(const char*,...);

void main() {
	float circum;
	printf("Circumference of circle: ");
	scanf("%f",&circum);
	printf("Radius is: %.1f\n",circum/(2*3.142));
}
