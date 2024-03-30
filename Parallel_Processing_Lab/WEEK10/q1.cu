// COMPLETE IT!!

#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define N 1024
#define len 100

// __global__ void mult(int *a, int *t, int c) {
//     int r = threadIdx.x;

//     for(int i=0; i<c; i++)
//         t[r*c+i] = pow(a[r*c+i], r+1);   // 3^1 is giving 2
  
// }

void display(int r, int c, int *t)
{
    int i, j;
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
            printf("%d\t",t[i*c+j]);
        printf("\n");
    }
}

void csr(int *m, int r, int c, int *data, int *colidx, int *rowptr, int *drr, int *kk)
{
    int i, j;
    int k=0, dr=0;
    for (i=0; i<r; i++)
    {
        rowptr[dr++]=k;
        for(j=0; j<c; j++)
        {
            int idx = i*c+j;
            if (m[idx]!=0)
            {
                data[k]=m[idx];
                colidx[k++]= c;
            }
        }
    }
    rowptr[dr]=k;
    *drr = dr;
    *kk = k;
}

int main() 
{
    int *a;
    int r, c, i;
    int *da, *dt;
    int dr, k;
    int data[len], rowptr[len], colidx[len];

    printf("Enter number of rows and columns: ");
    scanf("%d %d", &r, &c);

    int size = sizeof(int)*r*c;

    a = (int*)malloc(size);
    // t = (int*)malloc(size);

    printf("Enter the elements of the matrix: \n");
    for(i=0;i<r*c;i++)
        scanf("%d", &a[i]);


    // cudaMalloc((void**)&da, size);
    // cudaMalloc((void**)&dt, size);
    // cudaMemcpy(da, a, size, cudaMemcpyHostToDevice);
    // // cudaMemcpy(dt, t, size, cudaMemcpyHostToDevice);

    // // ROW-WISE
    // power<<<1,r>>>(da, dt, c);

    // cudaMemcpy(a, dt, size, cudaMemcpyDeviceToHost);
    // printf("\nResult:\n");
    // display(r,c,a);

    cudaFree(dt);
    cudaFree(da);    
    return 0;
}
