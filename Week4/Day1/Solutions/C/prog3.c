int printf(const char*,...);
int scanf(const char*,...);

void main(){
	float km;
	scanf("%f",&km);
	printf("%.0f km is equal to %.0fm\n",km,1000*km);
}
