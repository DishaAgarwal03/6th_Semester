// transpose of matrix

#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define N 1024

__global__ void power(int *a, int *t, int c) {
    int r = threadIdx.x;

    for(int i=0; i<c; i++)
        t[r*c+i] = pow(a[r*c+i], r+1);   // 3^1 is giving 2
  
}

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

int main() 
{
    int *a;
    int r, c, i;
    int *da, *dt;

    printf("Enter number of rows and columns: ");
    scanf("%d %d", &r, &c);

    int size = sizeof(int)*r*c;

    a = (int*)malloc(size);
    // t = (int*)malloc(size);

    printf("Enter the elements of the matrix: \n");
    for(i=0;i<r*c;i++)
        scanf("%d", &a[i]);


    cudaMalloc((void**)&da, size);
    cudaMalloc((void**)&dt, size);
    cudaMemcpy(da, a, size, cudaMemcpyHostToDevice);
    // cudaMemcpy(dt, t, size, cudaMemcpyHostToDevice);

    // ROW-WISE
    power<<<1,r>>>(da, dt, c);

    cudaMemcpy(a, dt, size, cudaMemcpyDeviceToHost);
    printf("\nResult:\n");
    display(r,c,a);

    cudaFree(dt);
    cudaFree(da);    
    return 0;
}
