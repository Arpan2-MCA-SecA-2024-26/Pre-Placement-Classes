// 8. Write a C program to search an x in array using pointers.

#include <stdio.h>

int searchElement(int *arr, int size, int x) {
    for (int i = 0; i < size; i++) {
        if (*(arr + i) == x)
            return i;
    }
    return -1;
}

int main() 
{
    int size, x, result;
    printf("Enter array size: ");
    scanf("%d", &size);
    int arr[size];
    printf("Enter array elements:\n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Enter the element to search: ");
    scanf("%d", &x);
    result = searchElement(arr, size, x);
    if (result != -1) {
        printf("Element %d found at index %d.\n", x, result);
    } 
	else {
        printf("Element %d not found in the array.\n", x);
    }
    return 0;
}
