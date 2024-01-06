#include "mpi.h"
#include<stdio.h>
void main(int argc, char *args[])
{
    int rank;

    MPI_Init(&argc, &args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank%2==0)
        printf("rank %d Hello\n",rank);
    else
        printf("rank %d World\n",rank);

    MPI_Finalize();

}