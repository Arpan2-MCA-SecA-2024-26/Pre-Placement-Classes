// 10. Write a C program to add two matrix and multiply two matrix using pointers.
// (b) For multiplying:

#include <stdio.h>
int main() 
{
    int r1,c1,r2,c2,i,j,k;
    printf("Enter rows and columns for the first matrix: ");
    scanf("%d %d", &r1, &c1);
    printf("Enter rows and columns for the second matrix: ");
    scanf("%d %d", &r2, &c2);
    if (c1 != r2) {
        printf("Matrix multiplication not possible. Columns of first matrix should be equal to rows of second matrix.\n");
        return -1;
    }
    int mat1[r1][c1], mat2[r2][c2], result[r1][c2];
    printf("Enter elements of the first matrix:\n");
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c1; j++) {
            printf("Element at [%d][%d]: ", i, j);
            scanf("%d", (*(mat1 + i) + j));
        }
    }
    printf("Enter elements of the second matrix:\n");
    for (i = 0; i < r2; i++) {
        for (j = 0; j < c2; j++) {
            printf("Element at [%d][%d]: ", i, j);
            scanf("%d", (*(mat2 + i) + j));
        }
    }
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c2; j++) {
            *(*(result + i) + j) = 0;
        }
    }
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c2; j++) {
            for (k = 0; k < c1; k++) {
                *(*(result + i) + j) += *(*(mat1 + i) + k) * *(*(mat2 + k) + j);
            }
        }
    }
    printf("Resultant Matrix after multiplication:\n");
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c2; j++) {
            printf("%d ", *(*(result + i) + j));
        }
        printf("\n");
    }
    return 0;
}
