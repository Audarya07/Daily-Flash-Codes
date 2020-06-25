int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int unit;
	float bill;
	printf("\nEnter units consumed = ");
	scanf("%d",&unit);
	if(unit<=50)
		bill = unit * 0.5;
	else if(unit <= 150)
		bill = 25 + ((unit-50)*0.75);
	else if(unit <= 250)
		bill = 100 + ((unit-150)*1.2);
	else if(unit > 250)
		bill = 220 + ((unit-250)*1.5);
	printf("Bill = %.2f\n",bill);
}
