import pandas as pd

data=pd.read_csv("data.csv")
print(data.describe())
pd.options.display.max_rows=999
# here in 7 row the value was 450 , which can't be possible that's why we will change that value to 45.
# data.loc[7,"Duration"]=45


#another method: using for loop to replacing all of the data 

for x in data.index:
    if data.loc[x,'Duration']>120:
        data.loc[x,"Duration"]=120
print(data)