#include "mpi.h"
#include<stdio.h>
#define size 4

void error(int ierr){
	int errclass,resultlen;
	char err_buffer[MPI_MAX_ERROR_STRING];

    if (ierr != MPI_SUCCESS) {
       MPI_Error_class(ierr,&errclass);
       MPI_Error_string(ierr,err_buffer,&resultlen);
       fprintf(stderr,"%s",err_buffer);
       MPI_Finalize();             
    }
}

void main(int argc, char *args[])
{
    int rank, n, i, j, ierr;
    int a[size][size], b[size][size]={0}, c[size][size]={0};
    int s;

    MPI_Init(&argc,&args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &n);
    MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);

    if (rank==0)
    {
        printf("Enter %d elements:\n", size*size);
        for(i=0; i<size; i++)
            for(j=0; j<size; j++)
                scanf("%d",&a[i][j]);
    }

    ierr = MPI_Bcast(a, size*size, MPI_INT, 0, MPI_COMM_WORLD);
    error(ierr);

    b[0][rank] = a[0][rank];
    for(i=1; i<size; i++)
        b[i][rank] += b[i-1][rank] + a[i][rank];

    ierr = MPI_Scan(b, c, size*size, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
    error(ierr);

    if (rank==n-1)
    {
        printf("Output matrix is:\n");
        for(i=0; i<size; i++)
        {
            for(j=0; j<size; j++)
                printf("%d ", c[i][j]);
            printf("\n");
        }
    }

    MPI_Finalize();
}