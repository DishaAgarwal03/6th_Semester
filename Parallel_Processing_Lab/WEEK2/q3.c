// Find better way
#include"mpi.h"
#include<stdio.h>
#include<stdlib.h>
void main(int argc, char*argv[])
{
    int rank,size;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Status status;
    if(rank==0)
    {
        int *buf;
        int a[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
        int bufsize = MPI_BSEND_OVERHEAD + sizeof(a);
        buf = (int*)malloc(bufsize);
        MPI_Buffer_attach(buf, bufsize);

        for (int i=0; i<size-1; i++)
            MPI_Bsend(&(a[i]), 1, MPI_INT, i+1, 1, MPI_COMM_WORLD);

        MPI_Buffer_detach(buf, &bufsize);
        fflush(stdout);
    }
    else
    {
        int x, val;
        MPI_Recv(&x,1,MPI_INT,0,1,MPI_COMM_WORLD, &status);

        if (rank%2==0) val = x*x;
        else val = x*x*x;

        fprintf(stdout,"Rank %d: received %d result: %d\n", rank, x, val);
        fflush(stdout);
    }

    MPI_Finalize();
}