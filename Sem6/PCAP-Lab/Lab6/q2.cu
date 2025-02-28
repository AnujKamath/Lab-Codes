// Write a program in CUDA to perform selection sort in parallel.
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>

__global__ void selection_sort_kernel(int *num, int *pos, int n)
{
    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n)
    {
        for (int j = 0; j < n; j++)
            if (num[j] < num[i])
                pos[i]++;
    }
}
__global__ void place_kernel(int *num, int *ans, int *pos, int n)
{
    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n)
    {
        ans[pos[i]] = num[i];
    }
}
void selection_sort(int *num, int *ans, int n)
{
    int pos[n] = {0};
    int *d_num, *d_pos, *d_ans;
    int size = sizeof(int);
    cudaMalloc((void **)&d_num, n * size);
    cudaMalloc((void **)&d_pos, n * size);
    cudaMalloc((void **)&d_ans, n * size);

    cudaMemcpy(d_num, num, n * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_pos, pos, n * size, cudaMemcpyHostToDevice);

    dim3 dimGrid(n, 1, 1);
    dim3 dimBlock(1, 1, 1);
    selection_sort_kernel<<<dimGrid, dimBlock>>>(d_num, d_pos, n);

    place_kernel<<<dimGrid, dimBlock>>>(d_num, d_ans, d_pos, n);
    cudaMemcpy(ans, d_ans, n * size, cudaMemcpyDeviceToHost);

    cudaFree(d_num);
    cudaFree(d_pos);
    cudaFree(d_ans);
}
int main()
{
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int num[n], ans[n];
    printf("\nEnter values of array N: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num[i]);
    }
    selection_sort(num, ans, n);
    printf("Sorted Array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", ans[i]);
    printf("\n");

    return 0;
}
// Enter size of array: 5

// Enter values of array N: 3 2 1 5 4
// Sorted Array: 1 2 3 4 5