int printf(const char*,...);
int scanf(const char*,...);


void main() {

	int i = 0,n,temp=0;
	char arr[10];
	printf("Enter Decimal number:");
	scanf("%d",&n);
    	while(n!=0) 
    	{    
        	temp = n%16; 
        	if(temp < 10) 
        	{ 
            		arr[i] = temp + 48; 
            		i++; 
        	} 
        	else
        	{ 
            		arr[i] = temp + 55; 
            		i++; 
        	} 
        	n /= 16; 
    	} 
    for(int j=i-1; j>=0; j--) 
        printf("%c",arr[j]);
   printf("\n"); 
}
