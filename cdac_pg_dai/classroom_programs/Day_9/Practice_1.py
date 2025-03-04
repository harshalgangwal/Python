import numpy as np
arr = np.arange(6)
print(arr)

rand_uniform = np.random.rand(3)    # Uniform distribution
rand_normal = np.random.randn(3)    # Normal distribution
rand_int = np.random.randint(1, 50, size=(3,3))  # Random integers
print(rand_uniform, rand_normal, rand_int)

arr = np.array([2, 7, 8, 9, 4])
print(np.sum(arr))        # Output: 15
print(np.mean(arr))       # Output: 3.0
print(np.median(arr))     # Output: 3.0
print(np.std(arr))        # Output: 1.4142135623730951 (Standard Deviation)

