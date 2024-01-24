#include "mpi.h"
#include<stdio.h>

void main(int argc, char *args[])
{
    int rank, n, m;
    int i, s=0;
    int a[20], c[10];
    float b[10], savg;

    MPI_Init(&argc,&args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &n);

    if (rank==0)
    {
        fprintf(stdout, "Enter m: ");
        fflush(stdout);
        scanf("%d", &m);
        fprintf(stdout, "Enter %d values: ", n*m);
        fflush(stdout);
        for(i=0;i<n*m;i++)
            scanf("%d", &a[i]);
    }
    MPI_Bcast(&m, 1, MPI_INT, 0, MPI_COMM_WORLD); 
    MPI_Scatter(a, m, MPI_INT, c, m, MPI_INT, 0, MPI_COMM_WORLD);
    for(i=0; i<m; i++)
        s += c[i];
    float avg = (float)s/m;
    MPI_Gather(&avg, 1, MPI_FLOAT, b, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

    if (rank==0)
    {
        savg = 0;
        for(i=0;i<n;i++)
            savg+=b[i];
        fprintf(stdout, "Result is %.2f\n", (float)savg/n);
        fflush(stdout);
    }

    MPI_Finalize();
}
