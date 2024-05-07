import numpy as np

array1 = np.arange(start=1, stop=10)
print('array1:', array1)

print('array1[2]:', array1[2])

print('맨 뒤의 값: ', array1[-1], '\n맨 뒤에서 두 번째 값: ', array1[-2])

array1[0] = 9
print(array1)

array2 = array1.reshape(3, 3)
print(array2)

print('1행 1열 값: ', array2[0, 0])
print('1행 2열 값: ', array2[0, 1])

#4차원 배열

array4 = np.random.randn(2, 2, 4, 5).round(3) #5개씩 1차원 배열이 4개, 1차원 배열 4개가 모인 2차원 배열이 2개, 2차원 배열 2개가 있는 3차원 배열이 2개
print(array4)

print("-"*45)

print('\n array4[0, 0]: \n', array4[0, 0])
print('\n array4[0, 1]: \n', array4[0, 1])
print('\n array4[1, 0]: \n', array4[1, 0])
print('\n array4[1, 0]: \n', array4[1, 1])

print("-"*45)

print('\n array4[0][1][3]: \n', array4[0][1][3])
print('\n array4[0][1][3][4]: \n', array4[0, 1, 3, 4]) #대괄호 대신 쉼표로도 차원 접근이 가능합니다.

# 슬라이싱
array1 = np.arange(start=1, stop = 10)
print(array1[0:2])

print(array1,'\n')
print(array1[:5])
print(array1[3:])
print(array1[:])

array1 = array1.reshape(3,3)
print(array1)
print('-'*10)

print(array1[0:2])