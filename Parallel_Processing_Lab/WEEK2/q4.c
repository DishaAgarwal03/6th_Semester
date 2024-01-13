#include"mpi.h"
#include<stdio.h>
void main(int argc, char*argv[])
{
    int rank,size;
    MPI_Status status;

    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);

    if(rank==0)
    {
        int x;
        printf("Enter a value in master process: ");
        scanf("%d",&x);

        x = x+1;
        MPI_Send(&x, 1, MPI_INT, rank+1, 1, MPI_COMM_WORLD);
        fprintf(stdout,"Rank %d: Sent %d\n",rank,x);

        MPI_Recv(&x,1,MPI_INT,size-1,1,MPI_COMM_WORLD, &status);
        fprintf(stdout,"Rank %d: received %d from rank %d\n", rank, x, size-1);
    }
    else
    {
        int x;

        MPI_Recv(&x,1,MPI_INT,rank-1,1,MPI_COMM_WORLD, &status);
        fprintf(stdout,"Rank %d: received %d from rank %d\n", rank, x, rank-1);

        x = x+1;
        MPI_Send(&x, 1, MPI_INT, (rank+1)%size, 1, MPI_COMM_WORLD);
    }

    MPI_Finalize();
}