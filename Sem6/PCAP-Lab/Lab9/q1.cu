// 1. Write a program in CUDA to perform parallel Sparse Matrix - Vector multiplication using com-
// pressed sparse row (CSR) storage format. Represent the input sparse matrix in CSR format in the
// host code.
#include <stdio.h>
#include <cuda_runtime.h>
int m, n;
#define cc 4
__global__ void csr_spmv(int m, int *row_ptr, int *col_idx, float *values, float *x, float *y)
{
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    if (row < m)
    {
        float sum = 0.0f;
        int start = row_ptr[row];
        int end = row_ptr[row + 1];
        for (int i = start; i < end; i++)
        {
            sum += values[i] * x[col_idx[i]];
        }
        y[row] = sum;
    }
}

void convert_to_csr(int m, int n, float dense_matrix[][cc],
                    int *&row_ptr, int *&col_idx, float *&values, int &nnz)
{
    nnz = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (dense_matrix[i][j] != 0)
                nnz++;

    row_ptr = new int[m + 1];
    col_idx = new int[nnz];
    values = new float[nnz];

    int current = 0;
    row_ptr[0] = 0;

    for (int i = 0; i < m; i++)
    {
        int row_nnz = 0;
        for (int j = 0; j < n; j++)
        {
            if (dense_matrix[i][j] != 0)
            {
                col_idx[current] = j;
                values[current] = dense_matrix[i][j];
                current++;
                row_nnz++;
            }
        }
        row_ptr[i + 1] = row_ptr[i] + row_nnz;
    }
}

int main()
{
    m = 4, n = 4;
    float dense_matrix[][cc] = {
        {1.0, 2.0, 0.0, 0.0},
        {0.0, 0.0, 3.0, 0.0},
        {0.0, 4.0, 0.0, 5.0},
        {0.0, 0.0, 6.0, 0.0}};

    int *row_ptr = nullptr, *col_idx = nullptr;
    float *values = nullptr;
    int nnz;
    convert_to_csr(m, n, dense_matrix, row_ptr, col_idx, values, nnz);

    float x[] = {1.0, 2.0, 3.0, 4.0};
    float y[m] = {0.0};

    int *d_row_ptr, *d_col_idx;
    float *d_values, *d_x, *d_y;

    cudaMalloc(&d_row_ptr, (m + 1) * sizeof(int));
    cudaMalloc(&d_col_idx, nnz * sizeof(int));
    cudaMalloc(&d_values, nnz * sizeof(float));
    cudaMalloc(&d_x, n * sizeof(float));
    cudaMalloc(&d_y, m * sizeof(float));

    cudaMemcpy(d_row_ptr, row_ptr, (m + 1) * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_col_idx, col_idx, nnz * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_values, values, nnz * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_x, x, n * sizeof(float), cudaMemcpyHostToDevice);

    int blocks = (m + 31) / 32;
    csr_spmv<<<blocks, 32>>>(m, d_row_ptr, d_col_idx, d_values, d_x, d_y);

    cudaMemcpy(y, d_y, m * sizeof(float), cudaMemcpyDeviceToHost);

    printf("Result vector:\n");
    for (int i = 0; i < m; i++)
    {
        printf("y[%d] = %.2f\n", i, y[i]);
    }

    cudaFree(d_row_ptr);
    cudaFree(d_col_idx);
    cudaFree(d_values);
    cudaFree(d_x);
    cudaFree(d_y);

    return 0;
}
// Result vector:
// y[0] = 5.00
// y[1] = 9.00
// y[2] = 28.00
// y[3] = 18.00