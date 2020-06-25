int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int num,ecnt=0,ocnt=0,rem,val;
	scanf("%d",&num);
	val=num;
	while(num){
		rem=num%10;
		num/=10;
		if(rem%2==0)
			ecnt+=1;
		else
			ocnt+=1;
	}
printf("The number %d contains %d odd and %d even digits\n",val,ocnt,ecnt);
}
