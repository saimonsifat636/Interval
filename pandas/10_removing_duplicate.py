import pandas as pd

data = pd.read_csv("text.csv", sep=r"\s+")
print(data.duplicated())

# if you want to remove all the duplicate then you can use this :
dataa=data.drop_duplicates()
print(dataa)