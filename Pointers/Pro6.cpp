// 6. Write a C program to swap two arrays using pointers.

#include <stdio.h>

void swapArrays(int *arr1, int *arr2, int size) {
    for (int i = 0; i < size; i++) {
        int temp = *(arr1 + i);
        *(arr1 + i) = *(arr2 + i);
        *(arr2 + i) = temp;
    }
}

int main() 
{
    int size;
    printf("Enter the size of the 2 arrays: ");
    scanf("%d", &size);
    int arr1[size], arr2[size];
    printf("Enter elements of the first array:\n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr1[i]);
    }
    printf("Enter elements of the second array:\n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr2[i]);
    }
    swapArrays(arr1, arr2, size);
    printf("After swapping:\n");
    printf("First array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\nSecond array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr2[i]);
    }
    return 0;
}
