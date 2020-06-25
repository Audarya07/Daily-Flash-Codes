int printf(const char*,...);
int scanf(const char*,...);

void main(){
	int i;
	for(i=1;i<=20;i++)
		printf("Cube of %d:%d\n",i,i*i*i);
}
