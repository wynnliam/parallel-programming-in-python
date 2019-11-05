"""
Liam Wynn, 9/26/2019, Simple PyCUDA Application

This is a simple PyCUDA application that demonstrates basic CUDA. It does as follows:
1. Creates an array on the CPU, then transfers it to the GPU.
2. Performs a task on the array in the GPU.
3. Returns the resulting array back to the CPU.

"""

import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

import numpy

a = numpy.random.randn(5, 5)
a = a.astype(numpy.float32)

a_gpu = cuda.mem_alloc(a.nbytes)
cuda.memcpy_htod(a_gpu, a)

mod = SourceModule("""
__global__ void doubles_matrix(float* a) {
    int idx = threadIdx.x + threadIdx.y * 4;
    a[idx] *= 2;
}
""")

func = mod.get_function("doubles_matrix")
func(a_gpu, block=(5,5,1))

a_doubled = numpy.empty_like(a)
cuda.memcpy_dtoh(a_doubled, a_gpu)

print("Original Matrix")
print(a)
print("Doubled Matrix")
print(a_doubled)