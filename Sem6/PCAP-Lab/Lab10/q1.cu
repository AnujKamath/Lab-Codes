// Question 1 Write a program in CUDA to perform matrix multiplication using 2D Grid and 2D Block.

#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>
#define WIDTH 2
__global__ void kernel_c(int *A, int *B, int *C)
{
    int row = blockDim.x * blockIdx.x + threadIdx.x;
    int col = blockDim.y * blockIdx.y + threadIdx.y;

    if (row < WIDTH && col < WIDTH)
    {
        int x = 0;
        for (int k = 0; k < WIDTH; k++)
            x += A[row * WIDTH + k] * B[k * WIDTH + col];
        C[row * WIDTH + col] = x;
    }
}
void mul_matrix(int A[][WIDTH], int B[][WIDTH])
{
    int C[WIDTH][WIDTH], size = sizeof(int);
    int *d_A, *d_B, *d_C;

    cudaMalloc((void **)&d_A, WIDTH * WIDTH * size);
    cudaMalloc((void **)&d_B, WIDTH * WIDTH * size);
    cudaMalloc((void **)&d_C, WIDTH * WIDTH * size);

    cudaMemcpy(d_A, A, WIDTH * WIDTH * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B, WIDTH * WIDTH * size, cudaMemcpyHostToDevice);

    kernel_c<<<dim3(ceil(WIDTH / 32.0), ceil(WIDTH / 32.0)), dim3(32, 32)>>>(d_A, d_B, d_C);

    cudaMemcpy(C, d_C, WIDTH * WIDTH * size, cudaMemcpyDeviceToHost);

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    printf("Resultant array:\n");
    for (int i = 0; i < WIDTH; i++)
    {
        for (int j = 0; j < WIDTH; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
}
int main()
{

    int A[WIDTH][WIDTH] = {{1, 2}, {2, 3}};
    int B[WIDTH][WIDTH] = {{3, 4}, {5, 6}};
    mul_matrix(A, B);
    return 0;
}
// Resultant array:
// 13 16
// 21 26