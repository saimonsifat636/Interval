# matrix[row,col]
# here we will learn how to access the row and col form a matrix using slicing  -> [start,end,step]


import numpy as np

array=np.array(
    [
     [1,2,3,4],
     [5,6,7,8],
     [10,11,12,13],
     [15,16,17,18]
    ]
    )

print(f"this will give the entire matrix or array: {array[0:]}")
print("\n\n")
print(f"this will give the rows till 2 : \n {array[0:3:2]}")
print("\n\n")
print(f"this will print every 2nd row : \n{array[0::2]}")
print("\n\n")
print(f"this will return the matrix in reverse order : \n{array[::-1]}")
print("\n\n")
print(f"this will give the first col: \n{array[:,0:1]}")
print("\n\n")
print(f"this will give a 2x2 matrix : \n{array[0:2,:2]}")
print("\n\n")
print(f"this will give mid 2 col matrix : \n{array[0:,1:3]}")
print("\n\n")
print(f"this will give a last two row 2x2 matrix : \n{array[2:,2:]}")