import pandas as pd
import numpy as np

# dictionary of lists
# data={
#     "name":['saim','katim','bisal','kikkk'],
#     "age":[23,44,55,12]
# }

# data=pd.DataFrame(data)
# print(dataa ,"\n\n\n")



# # list of dictionarys 
# data=[
#     {'name':'karim','age':23},
#     {'name':'kaka','age':53},
#     {'name':'rim','age':27}
#     ,{'name':'kam','age':83}
# ]

# dataa=pd.DataFrame(data)
# print(dataa ,"\n\n\n")


# #  using numpy array
# data=np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,12],
#     [2,3,5,2,6]
# ])

# data=pd.DataFrame(data,index=["row1","row2","row3"])
# print(data)


# printing first row 
data={
    "name":['saim','katim','bisal','kikkk'],
    "age":[23,44,55,12],
    "city":['dhaka','cht','shy','cu']
}

data=pd.DataFrame(data)


print(data.loc[0],"\n\n")
print(data.loc[[0,1,2]])  # -> selective kiso col er jonno eita use kora jabe