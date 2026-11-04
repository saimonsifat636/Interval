# in this we will find the dimention of the array

import numpy as np

'''array=np.array('a')

print(f"The dimention of this array is: {array.ndim}")    


array=np.array([1,23,3,4])

print(f"The dimention of this array is: {array.ndim}")    


array=np.array([
                [1,2,3,4],
                [5,6,7,8]
                ])

print(f"The dimention of this array is: {array.ndim}")    
'''

array=np.array([
    [[1,2,3,4],[5,6,7,8]],
    [[1,2,3,4],[5,6,7,8]],
    [[1,2,3,4],[5,6,7,8]],
    [[1,2,3,4],[5,6,7,8]]
    ])

print(f"The dimention of this array is: {array.ndim}")  #This will give the number of dimentions

print(f"[dept],[row],[col] : {array.shape}")  #this will give the arrays [dept],[row],[col]


    # we can access these array element using chain indexing and multidimentional indexing . chain index is slow but multidimentional indexing is faster.
    
print(f"using chain indexing [dept][row][col]: {array[0][0][0]}")
print(f"using multidimentionl indexing [dept,row,col]: {array[1,1,3]}")