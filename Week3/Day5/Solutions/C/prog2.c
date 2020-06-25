int printf(const char*,...);
int scanf(const char*,...);

void main() {
	float num;
	scanf("%f",&num);
	printf("Amount in dollar:%.4f\n",num/71.6);
}
