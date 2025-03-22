// Question 3. Write a CUDA program that reads a matrix A of size MXN and produce an output matrix B of
// same size such that it replaces all the non-border elements (numbers in bold) of A with its equivalent
// 1’s complement and remaining elements same as matrix A.

#include <stdio.h>
#include <cuda_runtime.h>
#include <math.h>
__device__ int complement(int val)
{
    int ans = 0, exp = 1;
    for (int i = val; i > 0; i /= 2, exp *= 10)
    {
        ans += (1 - (i % 2)) * exp;
    }
    return ans;
}
__global__ void computeRowExponents(int *in_mat, int *out_mat, int M, int N)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < M && col < N)
    {
        if (row == 0 || row == M - 1 || col == 0 || col == N - 1)
            out_mat[row * N + col] = in_mat[row * N + col];
        else
            out_mat[row * N + col] = complement(in_mat[row * N + col]);
    }
}

int main()
{
    int M, N;
    printf("Enter the dimension of matrix");
    scanf("%d %d", &M, &N);
    int matrix[M][N];
    printf("Enter %d elements", M * N);
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            scanf("%d", &matrix[i][j]);
    int output[M][N];

    int *d_matrix, *d_output;
    cudaMalloc((void **)&d_matrix, M * N * sizeof(int));
    cudaMalloc((void **)&d_output, M * N * sizeof(int));

    cudaMemcpy(d_matrix, matrix, M * N * sizeof(int), cudaMemcpyHostToDevice);

    dim3 blockSize(1, 1);
    dim3 gridSize(N, M);

    computeRowExponents<<<gridSize, blockSize>>>(d_matrix, d_output, M, N);

    cudaMemcpy(output, d_output, M * N * sizeof(int), cudaMemcpyDeviceToHost);

    printf("Modified matrix:\n");
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d\t", output[i][j]);
        }
        printf("\n");
    }

    cudaFree(d_matrix);
    cudaFree(d_output);
    return 0;
}
// Enter the dimension of matrix: 4 4
// 1 2 3 4 6 5 8 3 2 4 10 1 9 1 2 5
// Modified matrix:
// 1       2       3       4
// 6       10      111     3
// 2       11      101     1
// 9       1       2       5