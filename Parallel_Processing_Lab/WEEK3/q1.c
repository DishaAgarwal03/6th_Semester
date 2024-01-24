#include "mpi.h"
#include<stdio.h>

void main(int argc, char *args[])
{
    int rank;
    int n, a[10], b[10], c, i, s=0;

    MPI_Init(&argc,&args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &n);

    if (rank==0)
    {
        fprintf(stdout, "Enter %d values: ",n);
        fflush(stdout);
        for(i=0;i<n;i++)
            scanf("%d", &a[i]);
    }

    MPI_Scatter(a, 1, MPI_INT, &c, 1, MPI_INT, 0, MPI_COMM_WORLD);
    for(i=c-1; i>1; i--)
        c *= i;
    MPI_Gather(&c, 1, MPI_INT, b, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank==0)
    {
        for(i=0;i<n;i++)
            s+=b[i];
        fprintf(stdout, "Result is %d\n", s);
        fflush(stdout);
    }

    MPI_Finalize();
}
