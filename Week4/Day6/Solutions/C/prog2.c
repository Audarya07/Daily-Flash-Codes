int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i=0,num,arr[10];
	scanf("%d",&num);
	while(num!=0){
		arr[i] = num%8;
		num/=8;
		i++;
	}
	printf("Octal number:");
	for(int j=i-1;j>=0;j--)
		printf("%d",arr[j]);
	printf("\n");
}
