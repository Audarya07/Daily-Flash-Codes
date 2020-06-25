int printf(const char*,...);
int scanf(const char*,...);

#include<math.h>

void main() {
	int i,j,val=1;
	for(i=0;i<4;i++){
		for(j=0;j<=i;j++){
			printf("%.0f ",pow(val,3));
			val+=1;
		}
	printf("\n");
	}
}
