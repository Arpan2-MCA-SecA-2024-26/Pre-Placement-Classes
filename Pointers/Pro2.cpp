// 2. Write a C program to add two numbers using pointers.

#include <stdio.h>
int main() 
{
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    int *ptr1=&a,*ptr2=&b;
    printf("Sum = %d",*ptr1+*ptr2);
}
