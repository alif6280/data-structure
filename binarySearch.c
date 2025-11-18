#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
    int n,i,mid,high,low,item,temp,j;
    int com=0;

    printf("Enter number of array : ");
    scanf("%d",&n);

    int arr[n];
    srand(time(0));

    printf("Enter random numbers are : \n");
    for(i=0;i<n;i++)
    {
        arr[i]=rand() % 100;
        printf("%d ",arr[i]);
    }

    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    printf("\nSorted array is : \n");
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }

    printf("\nEnter item to search : ");
    scanf("%d",&item);

    low=0;
    high=n-1;

    while(low<=high)
    {
        mid=(low+high)/2;
        com++;
        if(arr[mid]==item)
        {
            printf("Item found at %d position and total compare is %d\n",mid+1,com);
            return 0;
        }
        else if(arr[mid]<item)
        low=mid+1;
        else
            high=mid-1;
    }
    printf("Item not found\n");
    return 0;
}
