#include "mpi.h"
#include<stdio.h>
#include<string.h>

void main(int argc, char *args[])
{
    int rank, n, len;
    int i, b[10];
    char str[100], rstr[100];
    char vowels[10] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    MPI_Init(&argc,&args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &n);

    if (rank==0)
    {
        fprintf(stdout, "Enter string whose length is divisible by %d: ",n);
        fflush(stdout);
        scanf("%[^\n]s", str);
        len = strlen(str)/n;
    }
    MPI_Bcast(&len, 1, MPI_INT, 0, MPI_COMM_WORLD); 
    MPI_Scatter(str, len, MPI_CHAR, rstr, len, MPI_CHAR, 0, MPI_COMM_WORLD);
    int nv = len;
    for(i=0; i<len; i++)
    {
        for(int j=0; j<10; j++)
        {
            if (rstr[i]==vowels[j])  // REMEMBER TO USE RSTR NOT STR
            {    
                nv--; break; 
            }
        }
    }
    MPI_Gather(&nv, 1, MPI_INT, b, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank==0)
    {
        int s = 0;
        for(i=0;i<n;i++)
        {
            fprintf(stdout, "%d ", b[i]);
            s+=b[i];
        }
        fprintf(stdout, "\nTotal number of non-vowels %d\n", s);
        fflush(stdout);
    }

    MPI_Finalize();
}
