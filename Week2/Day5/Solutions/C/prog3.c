int printf(const char*,...);
int scanf(const char *,...);
#include<math.h>

void main() {
	int i,num;
	scanf("%d",&num);
	for(i=1;i<num;i++)
		printf("Cube of %d : %.0f and Square of %d : %.0f\n",i,pow(i,3),i,pow(i,2));
printf("\n");
}
