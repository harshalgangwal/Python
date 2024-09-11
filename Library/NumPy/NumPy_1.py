# Creating NdArray
import numpy as np

a = np.array(7)
b = np.array([1, 2, 3, 4])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"0D Tensor/Scalar : {a}")
print(f"1D Tensor/Vector : {b}")
print(f"2D Tensor/Matrix : \n {c}")
print(f"3D Tensor/Tensor : \n {d}")
