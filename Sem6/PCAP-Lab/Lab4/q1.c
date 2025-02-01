// Write a MPI program using N processes to find 1! + 2! +.....+N!. Use scan. Also, handle
// different errors using error handling routines.
#include <stdio.h>
#include "mpi.h"
void ErrorHandler(int error_code)
{
    if(error_code!=MPI_SUCCESS)
    {
        char error_string[1000];
        int l,error_class;
        MPI_Error_class(error_code,&error_class);
        MPI_Error_string(error_code,error_string,&l);
        printf("%d %s \n", error_class, error_string);
    }
}
int main(int arge, char* argv[])
{ 
    int rank,b,size,fact=1, factsum, i;
    int error_code;
    MPI_Init(&arge, &argv);
    MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    error_code=MPI_Comm_size(MPI_COMM_WORLD, &size);
    ErrorHandler(error_code);

    b=rank+1;
    error_code=MPI_Scan(&b,&fact, 1, MPI_INT, MPI_PROD, MPI_COMM_WORLD);
    ErrorHandler(error_code);
    error_code=MPI_Reduce(&fact,&factsum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    ErrorHandler(error_code);

    if(rank==0)
    {
        printf("Sum of all the factorial=%d\n", factsum);
    }
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab4$ mpirun -n 4 ./out1
// 1073741824 Undefined dynamic error code 
// Sum of all the factorial=-1262468826
// 1073741824 Undefined dynamic error code 
// 1073741824 Undefined dynamic error code 
// 1073741824 Undefined dynamic error code 
