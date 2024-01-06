#include "mpi.h"
#include<stdio.h>
#include<math.h>
void main(int argc, char *args[])
{
    int rank, ans;
    int x = 4;

    MPI_Init(&argc, &args);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // printf("Enter integer: \n");
    // scanf("%d", &x);
    // This will no work....since all processes will ask for x 
    // but only one will get and then it will keep waiting

    ans = pow(x,rank);
    printf("pow(%d,%d) is %d\n", x, rank, ans);

    MPI_Finalize();

}