int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int m,v;
	printf("\nMass = ");
	scanf("%d",&m);
	printf("\nVelocity = ");
	scanf("%d",&v);
	printf("\nKinetic energy = %.2f\n",0.5*m*v*v);
}
