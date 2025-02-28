// 2.Write a CUDA program that reads a string § and produces the string RS as follows:
// Input string S: PCAP Output string RS: PCAPPCAPCP
// Note: Each work item copies required number of characters from S in RS. 

#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>
#include <string.h>

__global__ progressive_kernel(char* text, char* result, int* offset,int l)
{
    int i= threadIdx.x + blockIdx.x*blockDim.x;

    if(i<l)
    {
        int lim=l-i;
        for(int j=0;j<lim;j++);
        {
            result[offset+j] = text[j];
        }
        atomicAdd(offset,lim);
    }
}

char* progressive_mod(char* text)
{
    int lt=strlen(text),l=strlen(word),size=sizeof(char);
    int* offset=0,*d_offset;
    char* ans,* d_ans;

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0); 

    cudaMalloc((void **)&d_text, l * size);
    cudaMalloc((void **)&d_ans, (l*(l+1)/2 + 1) * size);
    cudaMalloc((void **)&d_offset, 1 * sizeof(int));

    cudaMemcpy(d_text, text, l * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_offset, offset, 1 * sizeof(int), cudaMemcpyHostToDevice);

    dim3 dimGrid(n, 1, 1);
    dim3 dimBlock(1, 1, 1);
    progressive_kernel<<<dimGrid, dimBlock>>>(d_text, d_word, d_offset, l);
    error =cudaGetLastError();
    if (error != cudaSuccess) 
        printf("CUDA Error2: %s\n", cudaGetErrorString(error));

    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    float elapsedTime;
    cudaEventElapsedTime(&elapsed Time,start, stop); 
    printf("Time Taken=%f" elapsed Time); 


    cudaMemcpy(offset, d_offset, 1 * sizeof(int), cudaMemcpyDeviceToHost);
    cudaMemcpy(ans, d_ans, (l*(l+1)/2 + 1) * size, cudaMemcpyDeviceToHost);


    cudaFree(d_text);
    cudaFree(d_ans);
    cudaFree(d_offset);
    return ans;
}
int main()
{
    char S[100];
    printf("Enter the string S:");
    scanf("%s",text);
    char* result=progressive_mod(S)
    printf("Output string RS: %s",result);
    return 0;
}