import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("data_now.csv" ,sep=r",")
data.plot(kind='scatter',x='Duration',y="Maxpulse")
plt.show()
data["Pulse"].plot(kind='hist')
plt.show()