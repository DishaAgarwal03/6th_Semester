

#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define N 1024

__global__ void power(int *a, int *t) {
    int r = blockDim.x;
    int c = blockDim.y;

    int p = 1, rev = 0, d;
    int ridx = threadIdx.x;
    int cidx = threadIdx.y;

    int i = ridx*c+cidx;
    if(ridx<r-1 && ridx>0 && cidx<c-1 && cidx>0)
    {
        int n = a[i];
        while (n>0)
        {
            d = n%2;
            d = (d==1)?0:1;
            rev += p*d;
            p *= 10;
            n /= 2;
        }
        t[i] = rev;
    }
    else 
        t[i] = a[i];
  
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
    int *a, *t;
    int r, c, i;
    int *da, *dt;

    printf("Enter number of rows and columns: ");
    scanf("%d %d", &r, &c);

    int size = sizeof(int)*r*c;

    a = (int*)malloc(size);
    t = (int*)malloc(size);

    printf("Enter the elements of the matrix: \n");
    for(i=0;i<r*c;i++)
        scanf("%d", &a[i]);


    cudaMalloc((void**)&da, size);
    cudaMalloc((void**)&dt, size);
    cudaMemcpy(da, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(dt, t, size, cudaMemcpyHostToDevice);

    // ELEMENT-WISE
    dim3 gd(1,1,1);
    dim3 bd(r,c,1); // writing this directly in the next statement is not working!!!!
    power<<<gd, bd>>>(da, dt);

    cudaMemcpy(t, dt, size, cudaMemcpyDeviceToHost);
    printf("\nResult:\n");
    display(r,c,t);

    cudaFree(dt);
    cudaFree(da);    
    return 0;
}
