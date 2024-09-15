// 10. Write a C program to add two matrix and multiply two matrix using pointers.
// (a) For adding:

#include <stdio.h>

void add(int *mat1, int *mat2, int *result, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            *(result + i * cols + j) = *(mat1 + i * cols + j) + *(mat2 + i * cols + j);
        }
    }
}
void disp(int *mat, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", *(mat + i * cols + j));
        }
        printf("\n");
    }
}

int main() 
{
    int rows = 2, cols = 2, i, j;
    int mat1[2][2], mat2[2][2], result[2][2];
    printf("Enter elements of first 2x2 matrix:\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            scanf("%d", &mat1[i][j]);
        }
    }
    printf("Enter elements of second 2x2 matrix:\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            scanf("%d", &mat2[i][j]);
        }
    }
    add((int *)mat1, (int *)mat2, (int *)result, rows, cols);
    printf("Resultant matrix after addition:\n");
    disp((int *)result, rows, cols);
    return 0;
}
