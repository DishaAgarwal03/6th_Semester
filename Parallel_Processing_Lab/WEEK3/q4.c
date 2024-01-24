#include "mpi.h"
#include<stdio.h>
#include<string.h>

void main(int argc, char *args[])
{
    int rank, n, len;
    int i;
    char b[100];  
    char s1[100], s2[100], rs1[100], rs2[100];
    char result[100];

    MPI_Init(&argc,&args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &n);

    if (rank==0)
    {
        fprintf(stdout, "Enter 2 strings whose length is divisible by %d: \n",n);
        fflush(stdout);
        scanf("%[^\n]s", s1);
        getchar();
        scanf("%[^\n]s", s2);
        len = strlen(s1)/n;
    }
    MPI_Bcast(&len, 1, MPI_INT, 0, MPI_COMM_WORLD); 
    MPI_Scatter(s1, len, MPI_CHAR, rs1, len, MPI_CHAR, 0, MPI_COMM_WORLD);
    MPI_Scatter(s2, len, MPI_CHAR, rs2, len, MPI_CHAR, 0, MPI_COMM_WORLD);

    // create alternating string - result
    int j = 0;
    for(i=0;i<len;i++)
    {
        result[j++]=rs1[i];
        result[j++]=rs2[i];  // REMEMBER TO USE RS2 NOT S2
    }

    MPI_Gather(result, len*2, MPI_CHAR, b, len*2, MPI_CHAR, 0, MPI_COMM_WORLD);

    if (rank==0)
    {
        b[len*2*n]='\0';
        fprintf(stdout, "\nResult: %s\n", b);
        fflush(stdout);
    }

    MPI_Finalize();
}
