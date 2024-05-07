import numpy as np


array1 = np.arange(start=1, stop = 10)

print(array1)
print('-'*10)

array1 = array1.reshape(3,3)
print(array1)
print(array1[1:, :2])


print(array1)
print('-'*10)

print(array1[[0,2]])
print('-'*10)

print(array1[[0,2], 1])
print('-'*10)

print(array1[[0,2], 0:2])

# 
boolean = array1[array1>3]

print('array1 > 3인 불린 인덱싱 결과 값:',  boolean)

print('객체반환: \n', array1>3)