int printf(const char*,...);
int scanf(const char*,...);

void main() {

    int ino = 0,newno = 0,digit = 1,fact = 1, i,num;
    scanf("%d",&num);
    for(i = 1; i <= num; i++)
    {
        ino = i;
        newno = 0;
        while(ino != 0)
        {
            fact = 1;
            digit = ino % 10;
            while(digit > 1)
            {
                fact *= digit--;            
            }
            newno += fact; 
            ino /= 10;
        }

        if(i == newno)
        printf("%d ",i);
    }
    printf("\n");
}
