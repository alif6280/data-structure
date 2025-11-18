#include<stdio.h>
#include<string.h>

int main()
{
    char str[100],oldword[100],newword[200];
    char result[1000];
    char *pos;

    printf("Enter any string : ");
    gets(str);
    printf("Enter replace to string : ");
    gets(oldword);
    printf("Enter new word to replace : ");
    gets(newword);

    pos=strstr(str,oldword);
    if(pos!='\0')
    {
        int index=pos-str;
        strncpy(result,str,index);
        result[index]='\0';

        strcat(result,newword);
        strcat(result,pos+strlen(oldword));

        printf("The replacement is : %s\n",result);
    }
    return 0;
}
