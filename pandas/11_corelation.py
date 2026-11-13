import pandas as pd

data=pd.read_csv("data_now.csv",sep=r",")
print(data)
print(data.corr(numeric_only=True))

# why use ...."corr()"........>>>>>>: this will give the relation between two col which will help us to find dependencies of two col. It also tell us If we change or drop any thing from one col how much other col will be affected. and the value is between (-1,1).