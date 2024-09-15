// 4. Write a C program to input and print array elements using pointer.

#include <stdio.h>
int main() 
{
    int n,i;
    printf("Enter array size: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter %d array elements:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Array elements are:\n");
    int *ptr = arr;
    for (i = 0; i < n; i++) {
        printf("%d ", *(ptr + i));
    }
    return 0;
}
