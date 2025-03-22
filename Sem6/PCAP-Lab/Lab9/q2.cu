// Question 2. Write a program in CUDA to read MXN matrix A and replace 1% row of this matrix by same
// elements, 2" row elements by square of each element and 3™ row elements by cube of each element
// and so on.

#include <stdio.h>
#include <cuda_runtime.h>
#include <math.h>
__global__ void computeRowExponents(int *matrix, int M, int N)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < M && col < N)
    {
        matrix[row * N + col] = (int)pow((float)matrix[row * N + col], (float)row + 1);
    }
}

int main()
{
    const int M = 3;
    const int N = 3;

    int h_matrix[M][N] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}};

    int *d_matrix;
    cudaMalloc((void **)&d_matrix, M * N * sizeof(int));

    cudaMemcpy(d_matrix, h_matrix, M * N * sizeof(int), cudaMemcpyHostToDevice);

    dim3 blockSize(1, 1);
    dim3 gridSize(N, M);

    computeRowExponents<<<gridSize, blockSize>>>(d_matrix, M, N);

    cudaMemcpy(h_matrix, d_matrix, M * N * sizeof(int), cudaMemcpyDeviceToHost);

    printf("Modified matrix:\n");
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d\t", h_matrix[i][j]);
        }
        printf("\n");
    }

    cudaFree(d_matrix);

    return 0;
}
// Modified matrix:
// 1       2       2
// 16      25      36
// 343     512     729