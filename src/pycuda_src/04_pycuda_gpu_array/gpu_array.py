import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np

a_gpu = gpuarray.to_gpu(np.random.randn(5, 5).astype(np.float32))
a_doubled = (2 * a_gpu).get()

print("ORIGINAL")
print(a_doubled)

print("DOUBLED MATRIX AFTER PyCUDA EXECUTION USING GPUARRAY CALL")
print(a_gpu)