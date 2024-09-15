// 3. Write a C program to swap two numbers using pointers.

#include <stdio.h>
int main() 
{
    int a,b,temp;
    printf("Enter two numbers: ");
    scanf("%d %d", &a,&b);
    printf("Before Swapping: a = %d and b = %d\n", a, b);
    int *ptr1 = &a, *ptr2 = &b;
    temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
    printf("After Swapping: a = %d and b = %d\n", a, b);
    return 0;
}
