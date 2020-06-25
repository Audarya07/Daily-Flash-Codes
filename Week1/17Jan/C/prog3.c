int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int age;
	char gen,mstatus;
	printf("\nEnter age = ");
	scanf("%d",&age);
	printf("\nEnter gender(M or F) = ");
	scanf(" %c",&gen);
	printf("\nEnter marital status(Y or N) = ");
	scanf(" %c",&mstatus);

	if(gen=='F')
		printf("Work only in urban areas..\n");
	else if(gen=='M' && (age>=20 && age<=40))
		printf("Work anywhere..\n");
	else if(gen=='M' && (age>40 && age<=60))
		printf("Work in urban areas only..\n");
	else
		printf("\nERROR..");
}
