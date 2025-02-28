// Question 1)Write a program in CUDA which performs convolution operation on one-dimensional input
// array N of size width using a mask array M of size mask_width to produce the resultant one-
// dimensional array P of size width.
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>

__global__ void convolution_1D_basic_kernel(float *N, float *M, float *P, int Mask_Width, int width)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < width)
    {
        float Pvalue = 0;
        int N_start_point = i - (Mask_Width / 2);
        for (int j = 0; j < Mask_Width; j++)
            if (N_start_point + j >= 0 && N_start_point + j < width)
                Pvalue += N[N_start_point + j] * M[j];
        P[i] = Pvalue;
    }
}
void convolution_1D(float *N, float *M, float *P, int Mask_Width, int width)
{
    float *d_n, *d_m, *d_p;
    int size = sizeof(float);
    cudaMalloc((void **)&d_n, width * size);
    cudaMalloc((void **)&d_m, Mask_Width * size);
    cudaMalloc((void **)&d_p, width * size);

    cudaMemcpy(d_n, N, width * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_m, M, Mask_Width * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_p, P, width * size, cudaMemcpyHostToDevice);

    float div = 1;
    dim3 dimGrid(ceil(width / div), 1, 1);
    dim3 dimBlock(div, 1, 1);
    convolution_1D_basic_kernel<<<dimGrid, dimBlock>>>(d_n, d_m, d_p, Mask_Width, width);

    cudaMemcpy(P, d_p, width * size, cudaMemcpyDeviceToHost);

    cudaFree(d_n);
    cudaFree(d_m);
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
// Enter size of array and Mask: 7 5

// Enter values of array N: 1 2 3 4 5 6 7

// Enter values of mask array:3 4 5 4 3
// Result: 22.00 38.00 57.00 76.00 95.00 90.00 74.00