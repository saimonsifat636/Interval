import pandas as pd

data = pd.read_csv("text.csv", sep=r"\s+")
data['Date'] = pd.to_datetime(data['Date'], format='mixed')

print(data)