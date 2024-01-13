#include "mpi.h"
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include <unistd.h>

void main(int argc, char *args[])
{
    int rank, size;
    MPI_Init(&argc,&args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    if (rank==0)
    {
        char s[] = "Hello, How Are You?";
        MPI_Ssend(s, 20, MPI_CHAR, 1, 1, MPI_COMM_WORLD);  
        // try strlen and sizeof -- see how it works
        // also try changing 20 to 1 and see how it reacts
        printf("Rank 0: String sent!\n");
        MPI_Recv(s, 20, MPI_CHAR, 1, 2, MPI_COMM_WORLD, &status);
        fprintf(stdout, "Rank 0: Received %s\n", s);
        fflush(stdout);
    }
    else
    {
        char s[20];
        MPI_Recv(s, 20, MPI_CHAR, 0, 1, MPI_COMM_WORLD, &status);
        printf("Rank 1: Received: %s\n", s);
        for(int i=0; i<strlen(s); i++)
        {
            if (isupper(s[i]))
                s[i] = tolower(s[i]);
            else
                s[i] = toupper(s[i]);
        }
        sleep(1);
        MPI_Ssend(s, 20, MPI_CHAR, 0, 2, MPI_COMM_WORLD);
        fprintf(stdout, "Rank 1: Sent %s\n", s);
        fflush(stdout);
    }
    MPI_Finalize();
}
