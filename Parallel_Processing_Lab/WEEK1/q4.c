// may use ctype.h - int isupper(int) and int toupper(int) - similar for lower
#include "mpi.h"
#include<stdio.h>
#include<string.h>
void main(int argc, char *args[])
{
    int rank, len;
    char s[100] = "HeLLo";
    len = strlen(s);

    MPI_Init(&argc, &args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    if (rank>=len)
        printf("No character present at rank %d\n", rank);
    else
    {
        if (s[rank]>=65 && s[rank]<=90)
            s[rank]+=32;
        else if (s[rank]>='a' && s[rank]<='z')
            s[rank]-=32;
        printf("Rank %d Modified string: %s\n",rank, s);
    }

    MPI_Finalize();

}