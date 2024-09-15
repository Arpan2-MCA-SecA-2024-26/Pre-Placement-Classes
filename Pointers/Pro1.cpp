// 1. Write a C program to create, initialize and use pointers.

#include <stdio.h>
int main() 
{
    int num = 10;
    int *ptr;
    ptr = &num;
    printf("The value of num: %d\n", num);
    printf("The value accessed using pointer: %d\n", *ptr);
    printf("The address of num: %p\n", &num);
    return 0;
}
