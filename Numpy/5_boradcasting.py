import numpy as np

arr1=np.array([[1,2,3,4,5]])
arr2=np.array([[1],[2],[3],[6],[4]])
# Here these array has different dimention . so to perform operation between them we need to follow some rule if       one's of row or col ==1 then we can perform otherwise it will fail.
print(arr1.shape)
print(arr2.shape)
print(arr1*arr2)


array1=np.array([[1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5]])

array2=np.array([[1],[2],[3],[6],[4]])

print(array1.shape)
print(array2.shape)
print(array2*array1)