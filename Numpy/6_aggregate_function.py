import numpy as np

# Aggregate functions = summarize data and give single values

arr=np.array([[1,2,3,4,100],
              [6,7,8,9,10]])

print(np.sum(arr))
print(np.mean(arr))  # Average
print(np.median(arr)) # middle value
print(np.var(arr))  # how much the values are squard speard form the mean.
print(np.std(arr))  # how much the values are squard root speard form the mean.
print(np.min(arr))  # minimum value
print(np.max(arr))  # maximum value
print(np.argmin(arr)) # this will return the index of the minimum value
print(np.argmax(arr)) # this will return the index of the maximum value
print(np.sum(arr , axis=0))  # this will sum all the col. as axis == 0
print(np.sum(arr , axis=1)) # this will sum all the rows. as axis == 1