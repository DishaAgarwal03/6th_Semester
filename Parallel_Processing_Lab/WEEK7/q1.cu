#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include<stdio.h>

__global__ void adda(int *a, int *b, int *c)
{
    int i = blockIdx.x;
    c[i] = a[i] + b[i];
}

__global__ void addb(int *a, int *b, int *c)
{
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
}

int main(void)
{
    int a[20],b[20],c[20];
    int *da, *db, *dc;
    int i, n;

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

    adda<<<n,1>>>(da, db, dc);
    cudaMemcpy(c, dc, size, cudaMemcpyDeviceToHost);
    printf("a) n blocks -> Result: ");
    for(i=0; i<n; i++)
        printf("%d ", c[i]);

    for(i=0;i<n;i++)
        c[i] = 0;
    addb<<<1,n>>>(da, db, dc);
    cudaMemcpy(c, dc, size, cudaMemcpyDeviceToHost);
    printf("\nb) n threads -> Result: ");
    for(i=0; i<n; i++)
        printf("%d ", c[i]);
    printf("\n");
    
    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);

    return 0;

}