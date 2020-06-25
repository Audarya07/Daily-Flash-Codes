int printf(const char*,...);
int scanf(const char*,...);

void main() {
	float hr;
	scanf("%f",&hr);
	printf("%.0f\n",hr*60*60);
}
