#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include<stdio.h>
#define t 5

__global__ void add(int *a, int *b, int *c)
{
    int i = blockIdx.x * t + threadIdx.x;
    c[i] = a[i] + b[i];
}

int main(void)
{
    int a[20],b[20],c[20];
    int *da, *db, *dc;
    int i, n, nb;

    printf("Enter size of array: ");
    scanf("%d", &n);
    printf("Enter elements of a and b: ");
    for(i=0; i<n*2; i++)
    {
        if (i<n)
            scanf("%d",&a[i]);
        else
            scanf("%d",&b[i-n]);
    }

    int size = sizeof(int)*n;
    cudaMalloc((void**)&da, size);
    cudaMalloc((void**)&db, size);
    cudaMalloc((void**)&dc, size);

    cudaMemcpy(da, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(db, b, size, cudaMemcpyHostToDevice);

    nb = ceil(n/(float)t);
    add<<<nb,t>>>(da, db, dc);
    cudaMemcpy(c, dc, size, cudaMemcpyDeviceToHost);
    printf("Result: ");
    for(i=0; i<n; i++)
        printf("%d ", c[i]);
    printf("\n");
    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);

    return 0;
}