int printf(const char*,...);
int scanf(const char*,...);

void main() {
	int i,j,n,x=7;
	for(i=0;i<4;i++){
            n=x;
            for(j=0;j<=i;j++){
                printf("%d ",n);
                n-=1;
            }
            x-=1;
            printf("\n");
        }
}

