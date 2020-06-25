int printf(const char*,...);
int scanf(const char*,...);
void main(){
	int r;
	float area;
	printf("\nEnter radius = ");
	scanf("%d",&r);
	area = 3.14 * r * r;
	printf("\nArea of circle = %.2f\n",area);
}
