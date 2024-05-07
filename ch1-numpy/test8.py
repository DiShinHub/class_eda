import numpy as np

# 행렬내적 
a = np.array([[1, 2, 3], [4, 5, 6]])
print('a행렬: \n', a)

b = np.array([[7, 8], [9, 10], [11, 12]])
print('b행렬: \n', b)

print('a와 b의 행렬내적 결과:\n', np.dot(a,b))


"""
[1, 2, 3][7, 9, 11] = 1 * 7 + 2 * 9 + 3 * 11 = 58
[1, 2, 3]*[8, 10, 12] = 1 * 8 + 2 * 10 + 3 * 12 = 64
[4, 5, 6]*[7, 9, 11] = 4 * 7 + 5 * 9 + 6 * 11 = 139
[4, 5, 6]*[8, 10, 12] = 4 * 8 + 5 * 10 + 6 * 12 = 154
"""

# 전치행렬
a = np.array([[1, 2], [3, 4]])
print('a행렬:\n', a)
print('a의 전치행렬:\n', np.transpose(a))

"""
a행렬:
 [[1 2]
 [3 4]]
a의 전치행렬:
 [[1 3]
 [2 4]]
"""

# 행렬 합산
a = np.array([[11, 12, 13], [2, 3, 4]])
print('a행렬:\n', a)
print('a+a =\n', a+a)

"""
a행렬:
 [[11 12 13]
 [ 2  3  4]]
a+a =
 [[22 24 26]
 [ 4  6  8]]
"""

# Broadcasting
print('a행렬:\n', a)
print('a+13=\n', a+13)
print('a-13=\n', a-13)
print('a*3=\n', a*3)

# add
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

print(a1, '\n+\n', a2, '\n=', a1+a2)

broad = np.arange(10).reshape(5, 2)
casting = np.arange(10, 12)

print(broad)
print('-'*10)
print(casting)
print('-'*10)
print(broad+casting)