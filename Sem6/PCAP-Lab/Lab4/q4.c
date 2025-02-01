// Write a MPI program to read a word of length N. Using N processes including the root get
// output word with the pattern as shown in example. Display the resultant output word in the
// root.
// Example: Input : PCAP Output : PCCAAAPPPP
#include <stdio.h>
#include "mpi.h"
int main(int argc, char* argv[])
{ 
    int rank,size,dest,d,idx;
    char str[10],res[100],buf,b[10];
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    if(rank==0)
    {
        printf("Enter the string:");
        scanf("%s",str);
    }
    MPI_Scatter(&str,1,MPI_CHAR,&buf,1,MPI_CHAR,0,MPI_COMM_WORLD);
    for(int i=0;i<=rank;i++)
        b[i]=buf;
    MPI_Send(&b,rank+1,MPI_CHAR,0,rank,MPI_COMM_WORLD);
    if(rank==0)
    {
        int c=0;
        for(int i=0;i<size;i++)
        {
            MPI_Recv(&str,i+1,MPI_CHAR,i,i,MPI_COMM_WORLD,&status);
            for(int j=0;j<i+1;j++)
                res[c++]=str[j];
        }
        res[c]='\0';
        printf("Resultant string\n");
        printf("%s \n",res);
    }
    MPI_Finalize();
    return 0;
}