int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int dist,time;
	printf("Distance(in m):");
	scanf("%d",&dist);
	printf("\nTime(in sec):");
	scanf("%d",&time);
	printf("\nThe velocity of particle:%.2f m/s\n",(float)dist/time);
}
