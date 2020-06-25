int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num;
	printf("Enter octal number:");
	scanf("%o",&num);

	printf("Hexadecimal number:%X\n",num);
}
