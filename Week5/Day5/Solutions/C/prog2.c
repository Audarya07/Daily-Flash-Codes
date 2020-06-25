int printf(const char*,...);
int scanf(const char*,...);

#include<string.h>

void main() {
	char hex[5];
	scanf("%s",hex);
	int len = strlen(hex);
	int base = 1,dec =0,bin[10],i=0,rem,cnt=0;
	for(int i = len-1;i>=0;i--){
		if(hex[i]>='0'&& hex[i]<='9'){
			dec += (hex[i]-48)*base;
		}	
		else if(hex[i]>='A'&& hex[i]<='F'){
			dec += (hex[i]-55)*base;
		}	
		base *=  16;
	}//Decimal number received in dec

	while(dec){
		rem=dec%2;
		dec/=2;
		bin[i] = rem;
		cnt+=1;	
		i++;
	}//Binary number received in bin[]

	printf("Decimal Number:");
	for(int j=cnt-1;j>=0;j--)
		printf("%d",bin[j]);
}
