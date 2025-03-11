// Question 1. Write a progrm in CUDA to add two Matrices for the following specifications:
// a.Each row of resultant matrix to be computed by one thread.
// b.Each column of resultant matrix to be computed by one thread.
// c.Each element of resultant matrix to be computed by one thread.

#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>
#define COL 3
__global__ void kernel_a(int *A, int *B, int *C, int r, int c)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < r)
    {
        for (int k = 0; k < c; k++)
        {
            int x = A[i * c + k] + B[i * c + k];

            C[i * c + k] = x;
        }
    }
}
__global__ void kernel_b(int *A, int *B, int *C, int r, int c)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < c)
    {
        for (int k = 0; k < r; k++)
        {
            C[c * k + i] = A[c * k + i] + B[c * k + i];
        }
    }
}
__global__ void kernel_c(int *A, int *B, int *C, int r, int c)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;

    if (i < r && j < c)
    {
        C[i * c + j] = A[i * c + j] + B[i * c + j];
    }
}
void add_matrix(int A[][COL], int B[][COL], int r, int c, int opt)
{
    int C[r][c], size = sizeof(int);
    int *d_A, *d_B, *d_C;

    cudaMalloc((void **)&d_A, r * c * size);
    cudaMalloc((void **)&d_B, r * c * size);
    cudaMalloc((void **)&d_C, r * c * size);

    cudaMemcpy(d_A, A, r * c * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B, r * c * size, cudaMemcpyHostToDevice);

    if (opt == 1)
        kernel_a<<<ceil(r / 32.0), 32>>>(d_A, d_B, d_C, r, c);
    else if (opt == 2)
        kernel_b<<<ceil(c / 32.0), 32>>>(d_A, d_B, d_C, r, c);
    else
        kernel_c<<<dim3(ceil(r / 32.0), ceil(c / 32.0)), dim3(32, 32)>>>(d_A, d_B, d_C, r, c);

    cudaMemcpy(C, d_C, r * c * size, cudaMemcpyDeviceToHost);

    cudaFree(d_A),
        cudaFree(d_B);
    cudaFree(d_C);
    printf("Resultant array:\n");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
}
int main()
{
    int r = 2, c = 3, option = 3;
    int A[r][COL] = {{1, 2, 3}, {4, 5, 6}};
    int B[r][COL] = {{5, 6, 9}, {15, 7, 15}};
    add_matrix(A, B, r, c, option);
    return 0;
}
