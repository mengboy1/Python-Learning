#测试numpy
import numpy as np
array = np.array([[1,2,3],[2,3,4]])
print(array)
print('number of dim:',array.ndim)
print('shape',array.shape)
print('size',array.size)

a = np.array([2,23,4],dtype=np.int64)
print(a.dtype)

a = np.zeros((3,4))
print(a)

a = np.ones((3,4),dtype=np.int)
print(a)

a = np.empty((3,4))
print(a)

a = np.arange(12).reshape((3,4))
print(a)

a = np.linspace(1,10,20).reshape((5,4))
print(a)
