// Question 3) Write a MPI program to read a string. Using N processes (string length is evenly divisible by
// N), find the number of non-vowels in the string. In the root process print number of non-
// vowels found by each process and print the total number of non-vowels.
#include "mpi.h"
#include <stdio.h>
#include <string.h>
int isVowel(char c)
{
    if(c>=65&&c<=90) c+=32;
    if(c!='a'&&c!='e'&&c!='i'&&c!='o'&&c!='u') return 0;
    return 1;
}
int main(int argc, char *argv[])
{
    int rank,size,N,l,i,chunk,non_vowel=0,C[10];
    char A[100], B[10];
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    if(rank==0)
    {
        N=size;
        printf("Enter the string: ");
        scanf("%s",A)
        l=strlen(A);
        chunk=l/N;
    }
    MPI_Bcast(&chunk,1,MPI_INT,0,MPI_COMM_WORLD);
    MPI_Bcast(&l,1,MPI_INT,0,MPI_COMM_WORLD);

    MPI_Scatter(A,chunk, MPI_CHAR,B,chunk,MPI_CHAR,0,MPI_COMM_WORLD);
    non_vowel=0;
    for(i=0;i<chunk;i++) 
    {
        if(!isVowel(B[i])) non_vowel++;
    }

    MPI_Gather(&non_vowel,1,MPI_INT,C,1,MPI_INT,0,MPI_COMM_WORLD);
    if(rank==0)
    {
        non_vowel=0;
        fprintf(stdout,"\nNo. of non-vowels found by each process: \n");
        for(i=0; i<N; i++)
        {
            fprintf(stdout,"%d \t",C[i]);
            non_vowel+=C[i];
        }
        fprintf(stdout,"\nTotal no. of non-vowels: %d\n",non_vowel);
    }
    fflush(stdout);
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab3$ mpirun -n 2 ./out1
// Enter the string: KaMATh

// No. of non-vowels found by each process: 
// 2 	2 	
// Total no. of non-vowels: 4

