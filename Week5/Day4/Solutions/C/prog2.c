int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int hex;
	printf("Hexadecimal number:");
	scanf("%X",&hex);
	printf("Decimal number:");
	printf("%d\n",hex);
}
