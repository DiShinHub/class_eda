import numpy as np

sequence_array = np.arange(10)
print(sequence_array)

zeros1 = np.zeros((3, 2))
print(zeros1)

zeros2 = np.zeros([3, 2])
print(zeros2)

ones1 = np.ones((3, 2))
print(ones1)

ones2 = np.ones([3, 2])
print(ones2)

rd = np.random.randn(3, 2) #중첩 괄호는 사용할 수 없습니다.
print(rd)
