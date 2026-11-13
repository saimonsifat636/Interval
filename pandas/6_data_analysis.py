import pandas as pd

data=pd.read_csv("data.csv")
print(data.head(10))    #->this will return the 1st ten rows from the file that helps us to analyse data 
print(data.tail())     #->this will return the last five rows by default 
print(data.tail(10))    #->this will return the last ten rows from the file that helps us to analyse data 
print(data.info())