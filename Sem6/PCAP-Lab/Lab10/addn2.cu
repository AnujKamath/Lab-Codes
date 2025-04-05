// Write a program in CUDA to perform tiled 1D convolution operation on the input array N of
// size width using the mask array, M of size mask_width, to produce the resultant array P of size
// width.
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>

#define TILE_SIZE 256
#define MASK_WIDTH 5

__global__ void tiled1DConvolution(float *N, float *M, float *P, int width, int mask_width)
{
    int global_index = blockIdx.x * blockDim.x + threadIdx.x;
    int half_mask = mask_width / 2;
    __shared__ float tile[TILE_SIZE + MASK_WIDTH - 1];
    int tile_start = blockIdx.x * blockDim.x;
    int local_index = threadIdx.x;
    int g_load = tile_start + local_index - half_mask;

    tile[local_index] = (g_load >= 0 && g_load < width) ? N[g_load] : 0.0f;

    if (threadIdx.x < mask_width - 1 && blockIdx.x < gridDim.x - 1)
    {
        int next_g_load = tile_start + blockDim.x + threadIdx.x - half_mask;
        tile[blockDim.x + threadIdx.x] = (next_g_load >= 0 && next_g_load < width) ? N[next_g_load] : 0.0f;
    }
    if (threadIdx.x >= blockDim.x - (mask_width - 1) && blockIdx.x > 0)
    {
        int prev_g_load = tile_start - (blockDim.x - threadIdx.x) - half_mask;
        tile[threadIdx.x - (blockDim.x - (mask_width - 1))] = (prev_g_load >= 0 && prev_g_load < width) ? N[prev_g_load] : 0.0f;
    }
    __syncthreads();

    if (global_index < width)
    {
        float sum = 0.0f;
        for (int k = 0; k < mask_width; ++k)
            sum += tile[local_index + k] * M[k];
        P[global_index] = sum;
    }
}

int main()
{
    int width = 7;
    int mask_width = MASK_WIDTH;

    float *d_N, *d_M, *d_P;
    float h_N[width] = {1, 2, 3, 4, 5, 6, 7};
    float h_M[mask_width] = {3, 4, 5, 4, 3};
    float h_P[width];
    cudaMalloc((void **)&d_N, width * sizeof(float));
    cudaMalloc((void **)&d_M, mask_width * sizeof(float));
    cudaMalloc((void **)&d_P, width * sizeof(float));
    cudaMemcpy(d_N, h_N, width * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_M, h_M, mask_width * sizeof(float), cudaMemcpyHostToDevice);
    int tpb = TILE_SIZE;
    int nb = (width + tpb - 1) / tpb;
    tiled1DConvolution<<<nb, tpb>>>(d_N, d_M, d_P, width, mask_width);
    cudaMemcpy(h_P, d_P, width * sizeof(float), cudaMemcpyDeviceToHost);

    printf("Input Array N:\n");
    for (int i = 0; i < width; ++i)
        printf("%.2f ", h_N[i]);
    printf("\n");

    printf("Mask M:\n");
    for (int i = 0; i < mask_width; ++i)
        printf("%.2f ", h_M[i]);
    printf("\n");

    printf("Resultant Array P:\n");
    for (int i = 0; i < width; ++i)
        printf("%.2f ", h_P[i]);
    printf("\n");

    cudaFree(d_N);
    cudaFree(d_M);
    cudaFree(d_P);
    return 0;
}

// Input Array N:
// 1.00 2.00 3.00 4.00 5.00 6.00 7.00
// Mask M:
// 3.00 4.00 5.00 4.00 3.00
// Resultant Array P:
// 22.00 38.00 57.00 76.00 95.00 90.00 74.00