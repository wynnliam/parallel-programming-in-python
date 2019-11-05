import numpy as np
from pycuda import driver, compiler, gpuarray, tools

import pycuda.autoinit

kernel_code_template = """
__global__ void matrix_mul_kernel(float* a, float* b, float* c) {
    int tx = threadIdx.x;
    int ty = threadIdx.y;
    
    float p_val = 0;
    float a_elem, b_elem;
    
    int k;
    for(k = 0; k < %(MATRIX_SIZE)s; ++k) {
        a_elem = a[ty * %(MATRIX_SIZE)s + k];
        b_elem = b[k * %(MATRIX_SIZE)s + tx];
        
        p_val += a_elem + b_elem;
    }
    
    c[ty * %(MATRIX_SIZE)s + tx] = p_val;
}
"""

MATRIX_SIZE = 5

a_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
b_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
c_cpu = np.dot(a_cpu, b_cpu)

a_gpu = gpuarray.to_gpu(a_cpu)
b_gpu = gpuarray.to_gpu(b_cpu)
c_gpu = gpuarray.empty((MATRIX_SIZE, MATRIX_SIZE), np.float32)

kernel_code = kernel_code_template % {
    'MATRIX_SIZE': MATRIX_SIZE
}

mod = compiler.SourceModule(kernel_code)

mat_mul = mod.get_function("matrix_mul_kernel")
mat_mul(a_gpu, b_gpu, c_gpu, block=(MATRIX_SIZE, MATRIX_SIZE, 1))

print("-" * 10)
print("Matrix A:")
print(a_gpu.get())
print("-" * 10)

print("-" * 10)
print("Matrix B:")
print(b_gpu.get())
print("-" * 10)

print("-" * 10)
print("Matrix C:")
print(c_gpu.get())
print("-" * 10)

print("-" * 10)
print("Matrix C Diff (CPU - GPU:")
print(c_cpu - c_gpu.get())
print("-" * 10)

np.allclose(c_cpu, c_gpu.get())
