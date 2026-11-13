import numpy as np

#Scalar arithmatic:

array=np.array([1,2,3,4])
print(array+1) # Here this array will act as a value 
print(array*2) # Here this array will act as a value 
print(array/2) # Here this array will act as a value 
print(array**2) # Here this array will act as a value 
print(array-5) # Here this array will act as a value 



#vectorized math function : in this we can also apply function on each element of that array
print("\n\nvectorized math function:")
print(np.sqrt(array))
array=np.sqrt(array)
print(np.round(array)) #this will return the round number close to their decimal point
print(np.floor(array)) #this will return the lower round number close to their decimal point
print(np.ceil(array)) # this will return the upper  number close to their decimal point
print(np.pi)




#Elementwise arithmatic:
arr1=np.array([1,2,3,4])
arr2=np.array([5,9,8,7])
print("\n\n Elementwise Arithmatic:  \n")
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr2/arr1)




#comparison operator:

result=np.array([55,99,100,33,44,88,66,77,22])
print("\n\ncomparison operator: \n")
print(result==100)
print(result>=33)
print(88>result)