#include "mpi.h"
#include<stdio.h>
void main(int argc, char *args[])
{
    int rank, x;
    int a = 20, b = 5;
    int arr[5]={'+', '-', '/', '*', '%'};
    MPI_Init(&argc, &args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    switch(rank)
    {
        case 0: x = a+b; break;
        case 1: x = a-b; break;
        case 2: x = a/b; break;
        case 3: x = a*b; break;
        case 4: x = a%b; break;
        default: printf("Rank %d: No operation\n", rank);
    }
    if (rank<5)
        printf("Rank %d: %d %c %d = %d\n", rank, a, arr[rank], b, x);

    MPI_Finalize();

}