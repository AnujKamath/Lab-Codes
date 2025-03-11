// Question 1. Write a progrm in CUDA to add two Matrices for the following specifications:
// a.Each row of resultant matrix to be computed by one thread.
// b.Each column of resultant matrix to be computed by one thread.
// c.Each element of resultant matrix to be computed by one thread.

#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>
#define COL 3
__global__ void kernel_a(int *A, int *B, int *C, int hA, int wA, int wB)
{
    int row = blockDim.x * blockIdx.x + threadIdx.x;
    if (row < hA)
    {
        for (int col = 0; col < wB; col++)
        {
            int x = 0;
            for (int k = 0; k < wA; k++)
            {
                x += A[row * wA + k] * B[k * wB + col];
            }
            C[row * wB + col] = x;
        }
    }
}
__global__ void kernel_b(int *A, int *B, int *C, int hA, int wA, int wB)
{
    int col = blockDim.x * blockIdx.x + threadIdx.x;
    if (col < wB)
    {
        for (int row = 0; row < hA; row++)
        {
            int x = 0;
            for (int k = 0; k < wA; k++)
            {
                x += A[row * wA + k] * B[k * wB + col];
            }
            C[row * wB + col] = x;
        }
    }
}
__global__ void kernel_c(int *A, int *B, int *C, int hA, int wA, int wB)
{
    int row = blockDim.x * blockIdx.x + threadIdx.x;
    int col = blockDim.y * blockIdx.y + threadIdx.y;

    if (row < hA && col < wB)
    {
        int x = 0;
        for (int k = 0; k < wA; k++)
            x += A[row * wA + k] * B[k * wB + col];
        C[row * wB + col] = x;
    }
}
void mul_matrix(int A[][COL], int B[][COL], int hA, int wA, int wB, int opt)
{
    int C[hA][wB], size = sizeof(int);
    int *d_A, *d_B, *d_C;

    cudaMalloc((void **)&d_A, hA * wA * size);
    cudaMalloc((void **)&d_B, wA * wB * size);
    cudaMalloc((void **)&d_C, hA * wB * size);

    cudaMemcpy(d_A, A, hA * wA * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B, wA * wB * size, cudaMemcpyHostToDevice);

    if (opt == 1)
        kernel_a<<<ceil(hA / 32.0), 32>>>(d_A, d_B, d_C, hA, wA, wB);
    else if (opt == 2)
        kernel_b<<<ceil(wB / 32.0), 32>>>(d_A, d_B, d_C, hA, wA, wB);
    else
        kernel_c<<<dim3(ceil(hA / 32.0), ceil(wB / 32.0)), dim3(32, 32)>>>(d_A, d_B, d_C, hA, wA, wB);

    cudaMemcpy(C, d_C, hA * wB * size, cudaMemcpyDeviceToHost);

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    printf("Resultant array:\n");
    for (int i = 0; i < hA; i++)
    {
        for (int j = 0; j < wB; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
}
int main()
{
    int hA = 2, wA = 3, wB = 3, option = 3;
    int A[hA][COL] = {{1, 2, 3}, {4, 5, 6}};
    int B[wA][COL] = {{5, 6, 9}, {15, 7, 15}, {2, 6, 4}};
    mul_matrix(A, B, hA, wA, wB, option);
    return 0;
}
// 1 2 3   5,6,9
// 4 5 6   15,7,15
//         2,6,4
