/*1) Write a MPI program using synchronous send. The sender process sends a word to the 
receiver. The second process receives the word, toggles each letter of the word and 
sends it back to the first process. Both processes use synchronous send operations.*/
#include <mpi.h>
#include <stdio.h>
#include <string.h>

int main(int argc,char* argv[])
{
    int rank, size;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Status status;
    if(rank==0)
    {
        char str[100];
        scanf("%s",str);
        int len=strlen(str);
        MPI_Ssend(&len,1,MPI_INT,1,1,MPI_COMM_WORLD);
        MPI_Ssend(&str,len,MPI_CHAR,1,1,MPI_COMM_WORLD);
        fprintf(stdout,"Initial String is: %s \n",str);


        MPI_Recv(&str,len,MPI_CHAR,1,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"Toggled String is: %s \n",str);
        fflush(stdout);

    }
    else if(rank==1)
    {
        char rstr[100];
        int l;
        MPI_Recv(&l,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
        MPI_Recv(&rstr,l,MPI_CHAR,0,1,MPI_COMM_WORLD,&status);

        for(int i=0;i<l;i++)
        {
            if(rstr[i]>96&&rstr[i]<123)
                rstr[i]-=32;
            else if(rstr[i]>64&&rstr[i]<91)
                rstr[i]+=32;
        }
        MPI_Ssend(&rstr,l,MPI_CHAR,0,1,MPI_COMM_WORLD);

    }
    MPI_Finalize();
    return 0;
}
// Initial String is: Anuj 
// Toggled String is: aNUJ 