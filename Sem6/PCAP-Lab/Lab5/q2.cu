// Implement a CUDA program to add two vectors of length N by keeping the number of
// threads per block as 256 (constant) and vary the number of blocks to handle N elements.
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>

__global__ void vecAddKernel(int *a, int *b, int *c, int n)
{
    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n)
        c[i] = a[i] + b[i];
}
void vecAdd(int *a, int *b, int *c, int n)
{
    int *d_a, *d_b, *d_c;
    int size = sizeof(int);
    cudaMalloc((void **)&d_a, n * size);
    cudaMalloc((void **)&d_b, n * size);
    cudaMalloc((void **)&d_c, n * size);

    cudaMemcpy(d_a, a, n * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b, n * size, cudaMemcpyHostToDevice);

    dim3 dimGrid(ceil(n / 256.0), 1, 1);
    dim3 dimBlock(256, 1, 1);
    vecAddKernel<<<dimGrid, dimBlock>>>(d_a, d_b, d_c, n);

    cudaMemcpy(c, d_c, n * size, cudaMemcpyDeviceToHost);

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
}
int main()
{
    int n = 5;
    int a[n], b[n], c[n];
    for (int i = 0; i < n; i++)
    {
        a[i] = i * 2;
        b[i] = i * i;
    }

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    for (int i = 0; i < n; i++)
        printf("%d ", b[i]);
    printf("\n");

    vecAdd(a, b, c, n);
    printf("Result: ");

    for (int i = 0; i < n; i++)
        printf("%d ", c[i]);
    printf("\n");

    return 0;
}