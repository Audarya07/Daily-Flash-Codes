int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,bin,hex=0,dec=0,base=1;
	printf("Enter binary number:");
	scanf("%d",&bin);
	while(bin){
		dec += (bin%10)*base;
		bin/=10;
		base*=2;	
	}
	printf("Decimal number = %d\n",dec);
	printf("Hexadecimal number = %X\n",dec);
}
