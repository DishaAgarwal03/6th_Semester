#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

#define t 5

__global__ void add(int *a, int *m, int *c, int n, int nm)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int mid = nm / 2;
  
    int sum = 0;
    for(int j = 0; j < nm; j++)
    {
        if(i + j - mid >= 0 && i + j - mid < n)
        {
            sum += a[i + j - mid] * m[j];
        }
    }

    c[i] = sum;
}

int main(void)
{
    int a[20], m[20], c[20];
    int *da, *dm, *dc;
    int n, nm;

    printf("Enter size of array and mask: ");
    scanf("%d %d", &n, &nm);
    printf("Enter elements of a and mask: \n");
    for(int i = 0; i < n + nm; i++)
    {
        if (i < n)
            scanf("%d", &a[i]);
        else
            scanf("%d", &m[i - n]);
    }

    int size_a = sizeof(int) * n;
    int size_m = sizeof(int) * nm;

    cudaMalloc((void**)&da, size_a);
    cudaMalloc((void**)&dm, size_m);
    cudaMalloc((void**)&dc, size_a);

    cudaMemcpy(da, a, size_a, cudaMemcpyHostToDevice);
    cudaMemcpy(dm, m, size_m, cudaMemcpyHostToDevice);

    int block_size = t;
    int grid_size = (n + block_size - 1) / block_size;

    add<<<grid_size, block_size>>>(da, dm, dc, n, nm);

    cudaMemcpy(c, dc, size_a, cudaMemcpyDeviceToHost);

    printf("Result: ");
    for(int i = 0; i < n; i++)
        printf("%d ", c[i]);
    printf("\n");

    cudaFree(da);
    cudaFree(dm);
    cudaFree(dc);

    return 0;
}
