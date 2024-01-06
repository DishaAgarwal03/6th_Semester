#include "mpi.h"
#include<stdio.h>
void main(int argc, char *args[])
{
    int rank, size;

    MPI_Init(&argc, &args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    printf("rank: %d and size: %d\n", rank, size);
    MPI_Finalize();

}