import numpy as np

org_array = np.array([4, 2, 8, 6])

print('원본 행렬: ', org_array)
print('np.sort 호출 후 반환된 행렬: ', np.sort(org_array))
print('np.sort 호출 후 원본 행렬: ', org_array)
print('ndarray.sort 호출 후 반환된 행렬:', org_array.sort())
print('ndarray.sort 호출 후 원본 행렬:', org_array)

print('내림차순 정렬: ', np.sort(org_array)[::-1])

array2 = np.array([[8, 1], [7, 12]])

print(array2)

print('열 방향 정렬:\n', np.sort(array2, axis = 1))
print('행 방향 정렬:\n', np.sort(array2, axis = 0))

org_array = np.array([4, 2, 8, 6])

print('np.argsort 호출 후 반환된 인덱스:', np.argsort(org_array))

print('np.argsort 호출 후 반환된 인덱스:', np.argsort(org_array)[::-1])