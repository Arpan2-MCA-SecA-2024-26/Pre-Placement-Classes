// 5. Write a C program to copy one array to another using pointers.

#include <stdio.h>
int main() 
{
    int n,i;
    printf("Enter array size: ");
    scanf("%d", &n);
    int arr1[n], arr2[n];
    printf("Enter %d elements of the first array:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr1[i]);
    }
    int *ptr1 = arr1, *ptr2 = arr2;
    for (i = 0; i < n; i++) {
        *(ptr2 + i) = *(ptr1 + i);
    }
    printf("Elements of the second array copied from the first array:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", arr2[i]);
    }
    return 0;
}
