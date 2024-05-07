import numpy as np

array1 = np.arange(10)
print("array1:\n", array1)

array2 = array1.reshape(2, 5) 
print("array2:\n", array2)

array1 = np.arange(8)

array3d = array1.reshape((2, 2, 2))
print('array3d: \n', array3d)

array2d = array3d.reshape(-1, 1)
print("array2d:\n", array2d)