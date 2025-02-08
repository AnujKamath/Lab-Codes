// Write a program in CUDA to process a 1D array containing angles in radians to generate
// sine of the angles in the output array. Use appropriate function.

#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>
#include <math.h>
__global__ void vecSineKernel(float *a, float *b, int n)
{
    size_t i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n)
        b[i] = sinf(a[i]);
}
void vecSine(float *a, float *b, int n)
{
    float *d_a, *d_b;
    int size = sizeof(float);
    cudaMalloc((void **)&d_a, n * size);
    cudaMalloc((void **)&d_b, n * size);

    cudaMemcpy(d_a, a, n * size, cudaMemcpyHostToDevice);

    dim3 dimGrid(ceil(n / 256.0), 1, 1);
    dim3 dimBlock(256, 1, 1);
    vecSineKernel<<<dimGrid, dimBlock>>>(d_a, d_b, n);

    cudaMemcpy(b, d_b, n * size, cudaMemcpyDeviceToHost);

    cudaFree(d_a);
    cudaFree(d_b);
}
int main()
{
    int n = 10;
    float a[n], b[n];
    for (int i = 0, c = 0; i < n; i++, c += 15)
    {
        a[i] = (c * M_PI) / 180;
    }
    printf("Radians: ");

    for (int i = 0; i < n; i++)
        printf("%.2f ", a[i]);
    printf("\n");

    vecSine(a, b, n);
    printf("Result : ");

    for (int i = 0; i < n; i++)
        printf("%.2f ", b[i]);
    printf("\n");

    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab5$ ./out1
// Radians: 0.00 0.26 0.52 0.79 1.05 1.31 1.57 1.83 2.09 2.36
// Result : 0.00 0.26 0.50 0.71 0.87 0.97 1.00 0.97 0.87 0.71
