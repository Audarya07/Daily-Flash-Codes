int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num;
	printf("Hexadecimal number:");
	scanf("%X",&num);
	printf("Ocatal number:%o\n",num);
}
