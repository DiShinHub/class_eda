import numpy as np

# 행렬 합산
a = np.array([[11, 12, 13], [2, 3, 4]])
print('a행렬:\n', a)
print(a.sum())

print('열 방향 합계: ', a.sum(axis=1))
print('행 방향 합계: ', a.sum(axis=0))

print(a.mean())

print(a.prod())

print(a.max())
print(a.min())

print(a)
print(a[1].max())
print(a[0].min())

print(a.argmax())
print(a.argmin())

print(a.std())
print(a.var())
