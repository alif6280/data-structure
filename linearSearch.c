#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
    int i,n,item;
    printf("Enter number of array : ");
    scanf("%d",&n);

    int arr[n],com=0;
    srand(time(0));
    for(i=0;i<n;i++)
    {
        arr[i]=rand() % 100;
    }

    printf("Random numbers are : \n");
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }

    printf("\nEnter item to search : ");
    scanf("%d",&item);

    for(i=0;i<n;i++)
    {
        com++;
        if(arr[i]==item)
        {
            printf("Item found at %d position and total compare %d\n",i+1,com);
            return 0;
        }
    }
    printf("Item not found\n",com);
    return 0;
}
