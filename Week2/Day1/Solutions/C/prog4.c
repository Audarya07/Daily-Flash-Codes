int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i,sum=0,x;
	float avg;
	for(i=0;i<10;i++){
		scanf("%d",&x);
		sum+=x;
	}
	avg=(float)sum/10;
	printf("Sum = %d\n",sum);
	printf("Average = %.2f\n",avg);
}
