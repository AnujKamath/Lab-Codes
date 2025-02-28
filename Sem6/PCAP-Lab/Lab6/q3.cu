// Write a program in CUDA to perform odd even transposition sort in parallel.
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>

__global__ void odd_sort_kernel(int *num, int n)
{
    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n - 1 && i % 2)
    {
        if (num[i] > num[i + 1])
        {
            int temp = num[i];
            num[i] = num[i + 1];
            num[i + 1] = temp;
        }
    }
}
__global__ void even_sort_kernel(int *num, int n)
{
    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n - 1 && i % 2 == 0)
    {
        if (num[i] > num[i + 1])
        {
            int temp = num[i];
            num[i] = num[i + 1];
            num[i + 1] = temp;
        }
    }
}
void oe_sort(int *num, int n)
{
    int *d_num;
    int size = sizeof(int);
    cudaMalloc((void **)&d_num, n * size);

    cudaMemcpy(d_num, num, n * size, cudaMemcpyHostToDevice);

    dim3 dimGrid(n, 1, 1);
    dim3 dimBlock(1, 1, 1);
    for (int i = 0; i < n / 2; i++)
    {
        odd_sort_kernel<<<dimGrid, dimBlock>>>(d_num, n);
        even_sort_kernel<<<dimGrid, dimBlock>>>(d_num, n);
    }
    cudaMemcpy(num, d_num, n * size, cudaMemcpyDeviceToHost);

    cudaFree(d_num);
}
int main()
{
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int num[n];
    printf("\nEnter values of array N: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num[i]);
    }
    oe_sort(num, n);
    printf("Sorted Array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", num[i]);
    printf("\n");

    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab6$ ./out1
// Enter size of array: 6

// Enter values of array N: 4 3 5 6 2
// 1
// Sorted Array: 1 2 3 4 5 6