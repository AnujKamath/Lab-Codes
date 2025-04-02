// Write a program in CUDA to improve the performance of 1D parallel convolution using constant
// Memory.
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>

__constant__ float d_M_constant[256];

__global__ void convolution_1D_constant_kernel(float *N, float *P, int Mask_Width, int width)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < width)
    {
        float Pvalue = 0;
        int N_start_point = i - (Mask_Width / 2);
        for (int j = 0; j < Mask_Width; j++)
        {
            if (N_start_point + j >= 0 && N_start_point + j < width)
            {
                Pvalue += N[N_start_point + j] * d_M_constant[j];
            }
        }
        P[i] = Pvalue;
    }
}

void convolution_1D(float *N, float *M, float *P, int Mask_Width, int width)
{
    float *d_n, *d_p;
    int size = sizeof(float);
    cudaMalloc((void **)&d_n, width * size);
    cudaMalloc((void **)&d_p, width * size);

    cudaMemcpy(d_n, N, width * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_p, P, width * size, cudaMemcpyHostToDevice);

    cudaMemcpyToSymbol(d_M_constant, M, Mask_Width * size);

    dim3 dimGrid(ceil(width / 32.0), 1);
    dim3 dimBlock(32, 1);

    convolution_1D_constant_kernel<<<dimGrid, dimBlock>>>(d_n, d_p, Mask_Width, width);

    cudaMemcpy(P, d_p, width * size, cudaMemcpyDeviceToHost);

    cudaFree(d_n);
    cudaFree(d_p);
}

int main()
{
    int m_width, width, i;
    printf("Enter size of array and Mask: ");
    scanf("%d", &width);
    scanf("%d", &m_width);
    float N[width], M[m_width], P[width];

    fflush(stdin);
    printf("\nEnter values of array N: ");
    fflush(stdin);

    for (int k = 0; k < width; k++)
    {
        scanf("%f", &N[k]);
    }

    printf("\nEnter values of mask array:");
    for (i = 0; i < m_width; i++)
        scanf("%f", &M[i]);

    convolution_1D(N, M, P, m_width, width);
    printf("Result: ");

    for (i = 0; i < width; i++)
        printf("%.2f ", P[i]);
    printf("\n");

    return 0;
}