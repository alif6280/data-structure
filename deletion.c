#include<stdio.h>
#include<string.h>

int main()
{
    char str[100],word[100];
    char result[1000];
    char *pos;

    printf("Enter any string : ");
    gets(str);
    printf("Enter delete to string : ");
    gets(word);

    pos=strstr(str,word);
    if(pos!='\0')
    {
        int index=pos-str;
        strncpy(result,str,index);
        result[index]='\0';

        strcat(result,pos+strlen(word));

        printf("The final string is : %s\n",result);
    }
    return 0;
}
