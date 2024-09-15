// 9. Write a C program to access two dimensional array using pointers.

#include <stdio.h>
int main() 
{
    int rows,cols,i,j;
    printf("Enter the number of rows and columns: ");
    scanf("%d %d", &rows, &cols);
    int arr[rows][cols];
    printf("Enter the elements of the matrix:\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            printf("Element at [%d][%d]: ", i, j);
            scanf("%d", (*(arr + i) + j));
        }
    }
    printf("Matrix is:\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            printf("%d ", *(*(arr + i) + j));
        }
        printf("\n");
    }
    return 0;
}
