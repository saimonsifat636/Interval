import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data_now.csv")
data.plot() #this will give a ploting diagram of the values
plt.show()