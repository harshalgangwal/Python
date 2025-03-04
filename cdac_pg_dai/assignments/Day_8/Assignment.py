import numpy as np
from numpy.linalg import eig
matrix = np.random.randint(10,size=(3,3))
values, vectors = eig(matrix)
# print(values)
# print(vectors)
combined = np.vstack(values,vectors)
print(combined)