import numpy as np

A = np.array([(1, 1, 2), (2, 4, -3), (3, 6, -5)])
B = np.array([(9), (1), (0)])

x = np.linalg.solve(A, B)
print(x)
