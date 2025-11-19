#include<stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
    int choice;
    int i,n;
    int arr[100],com=0;
    while(choice)
    {
        printf("\n====MENU====\n");
        printf("1. Create an Array\n");
        printf("2. Display the Array\n");
        printf("3. Insert the Array\n");
        printf("4. Delete the Array\n");
        printf("5. Exit\n");
        printf("\nEnter your choice : ");
        scanf("%d",&choice);

        if(choice==1)
        {
            printf("Enter number of array : ");
            scanf("%d",&n);
            srand(time(0));
            for(i=0;i<n;i++)
            {
               arr[i]=rand() % 100;
            }

            printf("Array created....!\n");
        }
        else if(choice==2)
        {
            if (n <= 0)
            {
                printf("\nArray is empty!\n");
                continue;
            }
            printf("The %d Numbers are :\n",n);
            for (i = 0; i < n; i++)
            {
                printf("%3d",arr[i]);
            }
            printf("\n");
        }
        else if(choice==3)
        {
            int pos,value;
            if(n>=100)
            {
                printf("Array is full ! Cannot insert array.\n");
                continue;
            }
            printf("Enter position to insert : ");
            scanf("%d",&pos);
            printf("Enter element to insert : ");
            scanf("%d",&value);
            for(i=n;i>pos;i--)
            {
                arr[i]=arr[i-1];
            }
            arr[pos]=value;
            n++;
            printf("Value inserted Successfull....!\n");
            printf("Updated Array: ");
            for(i=0;i<n;i++)
            {
                printf("%3d", arr[i]);
            }
            printf("\n");
        }
        else if(choice==4)
        {
            int pos;
            if(n<=0)
            {
                printf("Array is empty ! Nothing to delete.\n");
                continue;
            }
            printf("Enter position to delete : ");
            scanf("%d",&pos);
            for(i=pos;i<n-1;i++)
            {
                arr[i]=arr[i+1];
            }
            n--;
            printf("Array delete successfully......!\n");
            printf("Updated Array: ");
            for(i=0;i<n;i++)
            {
                printf("%3d", arr[i]);
            }
            printf("\n");
        }
        else if(choice==5)
        {
            printf("Exiting program......!\n");
            break;
        }
        else
        {
            printf("Invalid Choice!Try Again.....\n");
        }
    }
}


