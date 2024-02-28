#include "cuda_runtime.h"
#include <math.h>
#include "device_launch_parameters.h"
#include<stdio.h>

__global__ void add(int *a, float *b)
{
    int i = threadIdx.x;
    b[i] = sinf(a[i]);
}

int main(void)
{
    int a[20];
    float b[20];
    int *da;
    float *db;
    int i, n;

    printf("Enter size of array: ");
    scanf("%d", &n);
    printf("Enter %d angles as radians: ",n);
    for(i=0; i<n; i++)
        scanf("%d",&a[i]);

    int size = sizeof(int)*n;
    int sizef = sizeof(float)*n;
    cudaMalloc((void**)&da, size);
    cudaMalloc((void**)&db, sizef);

    cudaMemcpy(da, a, size, cudaMemcpyHostToDevice);
    add<<<1,n>>>(da, db);
    cudaMemcpy(b, db, sizef, cudaMemcpyDeviceToHost);

    printf("Result: ");
    for(i=0; i<n; i++)
        printf("%f ", b[i]);
    printf("\n");

    cudaFree(da);
    cudaFree(db);

    return 0;
}