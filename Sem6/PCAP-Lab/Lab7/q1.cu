// 1. Write a program in CUDA to count the number of times a given word is repeated in a sentence.
// (Use Atomic function)
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <cuda.h>
#include <string.h>

__global__ count_occur_kernel(char* text, char* word, int* count,int lt,int lw)
{
    int i= threadIdx.x + blockIdx.x*blockDim.x;
    if(i<lt-lw)
    {
        int check=1;
        for(int  j=0;j<lw && text[i+j]==word[j];j++);
        {
            if(text[i+j]!=word[j])
            {
                check=0;break;
            }
        }
        if(check)
            atomicAdd(count,1);
    }
}

int count_occur(char* text, char* word)
{
    int lt=strlen(text),lw=strlen(word),size=sizeof(int);
    int* count=0,*d_count;
    char* d_text;

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0); 

    cudaMalloc((void **)&d_text, lt * sizeof(char));
    cudaMalloc((void **)&d_count, 1 * size);
    cudaMemcpy(d_text, text, lt * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_count, count, 1 * size, cudaMemcpyHostToDevice);

    dim3 dimGrid(n, 1, 1);
    dim3 dimBlock(1, 1, 1);
    count_occur_kernel<<<dimGrid, dimBlock>>>(d_text, word, d_count, lt,lw);
    error =cudaGetLastError();
    if (error != cudaSuccess) 
        printf("CUDA Error2: %s\n", cudaGetErrorString(error));

    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    float elapsedTime;
    cudaEventElapsedTime(&elapsed Time,start, stop); 
    printf("Time Taken=%f" elapsed Time); 


    cudaMemcpy(count, d_count, 1 * size, cudaMemcpyDeviceToHost);

    cudaFree(d_text);
    cudaFree(d_count);
    return *count;
}
int main()
{
    char text[100], word[10];
    int lt,lw;
    printf("Enter the sentence");
    scanf("%s",text);
    lt=strlen(text);
    printf("Enter the word to be searched");
    scanf("%s",word);
    lw=strlen(word);
    int result = count_occur(text,word);
    printf("Total no. of occurrences of %s in text is= %d", text, result);
    return 0;



}