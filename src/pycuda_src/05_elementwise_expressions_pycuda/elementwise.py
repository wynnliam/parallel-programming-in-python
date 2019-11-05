import pycuda.gpuarray as gpuarray
import pycuda.autoinit
import numpy as np

from pycuda.curandom import rand as curand
from pycuda.elementwise import ElementwiseKernel
import numpy.linalg as la

input_vect_a = curand((50, ))
input_vect_b = curand((50, ))

mult_coefficient_a = 2
mult_coefficient_b = 5

linear_combo = ElementwiseKernel(
    "float a, float *x, float b, float *y, float *c",
    "c[i] = a * x[i] + b * y[i]",
    "linear_combination"
)

linear_combo_result = gpuarray.empty_like(input_vect_a)
linear_combo(mult_coefficient_a, input_vect_a,
             mult_coefficient_b, input_vect_b,
             linear_combo_result)

print("INPUT VECTOR A = ")
print(input_vect_a)

print("INPUT VECTOR B = ")
print(input_vect_b)

print("RESULT VECTOR C = ")
print(linear_combo_result)
